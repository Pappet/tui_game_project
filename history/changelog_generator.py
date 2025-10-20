#!/usr/bin/env python3
"""
Changelog Generator for TUI RPG Game
Parses version history files and generates a comprehensive changelog.
"""

import re
import json
from pathlib import Path
from typing import List, Dict, Any
from dataclasses import dataclass
from datetime import datetime


@dataclass
class FileChange:
    """Represents a change to a file"""
    path: str
    status: str
    agent: str
    action: str  # 'added', 'modified', 'finalized'


@dataclass
class VersionInfo:
    """Represents a version in the history"""
    version: str
    files: List[Dict[str, Any]]
    decisions: List[str]
    next_step: Dict[str, Any]
    completion_status: Dict[str, str]


class ChangelogGenerator:
    def __init__(self, history_dir: str = "."):
        self.history_dir = Path(history_dir)
        self.versions: List[VersionInfo] = []
        
    def load_versions(self):
        """Load all version files"""
        version_files = sorted(self.history_dir.glob("v*.txt"))
        
        for file_path in version_files:
            print(f"📖 Loading {file_path.name}...")
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                version_info = self._parse_version(content, file_path.name)
                if version_info:
                    self.versions.append(version_info)
        
        print(f"✅ Loaded {len(self.versions)} versions\n")
    
    def _parse_version(self, content: str, filename: str) -> VersionInfo:
        """Parse a version file and extract structured data"""
        # Extract JSON from PROJECT STATE section
        json_pattern = r'```json\s*\n(\{[\s\S]*?\n\})\s*\n```'
        matches = re.findall(json_pattern, content)
        
        if not matches:
            print(f"⚠️  No JSON found in {filename}")
            return None
        
        # Take the last (most complete) JSON block
        try:
            data = json.loads(matches[-1])
            return VersionInfo(
                version=data.get('version', 'unknown'),
                files=data.get('files', []),
                decisions=data.get('decisions', []),
                next_step=data.get('next_step', {}),
                completion_status=data.get('completion_status', {})
            )
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing JSON in {filename}: {e}")
            return None
    
    def _compare_versions(self, prev: VersionInfo, current: VersionInfo) -> List[FileChange]:
        """Compare two versions and detect changes"""
        changes = []
        
        # Create lookup for previous files
        prev_files = {f['path']: f for f in prev.files}
        
        for file in current.files:
            path = file['path']
            prev_file = prev_files.get(path)
            
            if not prev_file:
                # New file
                changes.append(FileChange(
                    path=path,
                    status=file['status'],
                    agent=file.get('last_agent', 'unknown'),
                    action='added'
                ))
            elif prev_file['status'] != file['status']:
                # Status changed
                if file['status'] == 'final':
                    action = 'finalized'
                elif file['status'] == 'awaiting_review':
                    action = 'updated'
                else:
                    action = 'modified'
                
                changes.append(FileChange(
                    path=path,
                    status=file['status'],
                    agent=file.get('last_agent', 'unknown'),
                    action=action
                ))
        
        return changes
    
    def _get_new_decisions(self, prev: VersionInfo, current: VersionInfo) -> List[str]:
        """Find new decisions made in this version"""
        prev_decisions = set(prev.decisions)
        return [d for d in current.decisions if d not in prev_decisions]
    
    def _categorize_changes(self, changes: List[FileChange]) -> Dict[str, List[FileChange]]:
        """Categorize changes by type"""
        categories = {
            'core': [],
            'ui': [],
            'logic': [],
            'data': [],
            'other': []
        }
        
        for change in changes:
            if 'core/' in change.path:
                categories['core'].append(change)
            elif 'tui/' in change.path or 'screens/' in change.path:
                categories['ui'].append(change)
            elif 'game_logic/' in change.path:
                categories['logic'].append(change)
            elif 'data/' in change.path:
                categories['data'].append(change)
            else:
                categories['other'].append(change)
        
        return categories
    
    def _get_emoji(self, action: str, category: str) -> str:
        """Get appropriate emoji for change type"""
        emoji_map = {
            'added': {
                'core': '🎯',
                'ui': '🎨',
                'logic': '⚙️',
                'data': '📦',
                'other': '✨'
            },
            'finalized': '✅',
            'updated': '🔧',
            'modified': '📝'
        }
        
        if action in ['finalized', 'updated', 'modified']:
            return emoji_map[action]
        return emoji_map['added'].get(category, '✨')
    
    def _format_change(self, change: FileChange, category: str) -> str:
        """Format a single change line"""
        emoji = self._get_emoji(change.action, category)
        filename = Path(change.path).name
        
        action_text = {
            'added': 'Added',
            'finalized': 'Completed',
            'updated': 'Updated',
            'modified': 'Modified'
        }
        
        return f"{emoji} {action_text[change.action]} `{filename}`"
    
    def generate_markdown(self) -> str:
        """Generate the complete changelog in Markdown format"""
        lines = [
            "# 📋 Changelog",
            "",
            f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*",
            "",
            "---",
            ""
        ]
        
        # Reverse to show newest first
        for i in range(len(self.versions) - 1, 0, -1):
            current = self.versions[i]
            prev = self.versions[i - 1]
            
            lines.append(f"## {current.version}")
            lines.append("")
            
            # Get changes
            changes = self._compare_versions(prev, current)
            new_decisions = self._get_new_decisions(prev, current)
            
            if not changes and not new_decisions:
                lines.append("*No significant changes*")
                lines.append("")
                continue
            
            # Categorize changes
            categorized = self._categorize_changes(changes)
            
            # Core changes
            if categorized['core']:
                lines.append("### Core System")
                for change in categorized['core']:
                    lines.append(f"- {self._format_change(change, 'core')}")
                lines.append("")
            
            # UI changes
            if categorized['ui']:
                lines.append("### User Interface")
                for change in categorized['ui']:
                    lines.append(f"- {self._format_change(change, 'ui')}")
                lines.append("")
            
            # Logic changes
            if categorized['logic']:
                lines.append("### Game Logic")
                for change in categorized['logic']:
                    lines.append(f"- {self._format_change(change, 'logic')}")
                lines.append("")
            
            # Data changes
            if categorized['data']:
                lines.append("### Data & Configuration")
                for change in categorized['data']:
                    lines.append(f"- {self._format_change(change, 'data')}")
                lines.append("")
            
            # Other changes
            if categorized['other']:
                lines.append("### Other")
                for change in categorized['other']:
                    lines.append(f"- {self._format_change(change, 'other')}")
                lines.append("")
            
            # New decisions
            if new_decisions:
                lines.append("### 💡 Decisions")
                for decision in new_decisions:
                    lines.append(f"- {decision}")
                lines.append("")
            
            # Next steps
            if current.next_step:
                task = current.next_step.get('task', 'Unknown')
                # Truncate if too long
                if len(task) > 100:
                    task = task[:97] + "..."
                lines.append(f"**Next:** {task}")
                lines.append("")
            
            # Completion status
            status = current.completion_status
            status_items = [f"{k}: {v}" for k, v in status.items() if v not in ['not_started', 'pending']]
            if status_items:
                lines.append(f"*Status: {', '.join(status_items)}*")
                lines.append("")
            
            lines.append("---")
            lines.append("")
        
        # Add initial version info
        if self.versions:
            first = self.versions[0]
            lines.append(f"## {first.version} - Initial Setup")
            lines.append("")
            lines.append("🎬 Project initialization")
            lines.append("")
            lines.append("### Initial Decisions")
            for decision in first.decisions:
                lines.append(f"- {decision}")
            lines.append("")
        
        return "\n".join(lines)
    
    def generate_compact_changelog(self) -> str:
        """Generate a compact version for quick overview"""
        lines = [
            "# 📋 Changelog (Compact)",
            "",
            "Quick overview of major milestones:",
            ""
        ]
        
        for i in range(len(self.versions) - 1, 0, -1):
            current = self.versions[i]
            prev = self.versions[i - 1]
            
            changes = self._compare_versions(prev, current)
            finalized = [c for c in changes if c.action == 'finalized']
            
            if finalized or i == len(self.versions) - 1:  # Latest or has completions
                task = current.next_step.get('task', 'Development continues')
                if len(task) > 80:
                    task = task[:77] + "..."
                
                lines.append(f"**{current.version}** - {task}")
                
                if finalized:
                    lines.append(f"  - ✅ Completed {len(finalized)} file(s)")
                lines.append("")
        
        return "\n".join(lines)
    
    def save_changelog(self, filename: str = "CHANGELOG.md"):
        """Save the generated changelog to a file"""
        output_path = self.history_dir / filename
        changelog = self.generate_markdown()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(changelog)
        
        print(f"✅ Changelog saved to: {output_path}")
        
        # Also save compact version
        compact_path = self.history_dir / "CHANGELOG_COMPACT.md"
        compact = self.generate_compact_changelog()
        with open(compact_path, 'w', encoding='utf-8') as f:
            f.write(compact)
        
        print(f"✅ Compact changelog saved to: {compact_path}")
        
        return output_path
    
    def print_summary(self):
        """Print a summary of the project evolution"""
        if not self.versions:
            print("No versions loaded")
            return
        
        latest = self.versions[-1]
        
        print("\n" + "="*60)
        print("📊 PROJECT SUMMARY")
        print("="*60)
        print(f"Current Version: {latest.version}")
        print(f"Total Versions: {len(self.versions)}")
        print(f"Total Files: {len(latest.files)}")
        print(f"Total Decisions: {len(latest.decisions)}")
        print()
        print("Completion Status:")
        for key, value in latest.completion_status.items():
            emoji = "✅" if value == "done" else "🚧" if value == "in_progress" else "⏳"
            print(f"  {emoji} {key.replace('_', ' ').title()}: {value}")
        print()
        
        # File status distribution
        status_count = {}
        for file in latest.files:
            status = file['status']
            status_count[status] = status_count.get(status, 0) + 1
        
        print("File Status Distribution:")
        for status, count in sorted(status_count.items()):
            print(f"  - {status}: {count}")
        print("="*60 + "\n")


def main():
    """Main entry point"""
    print("🚀 TUI RPG Changelog Generator")
    print("="*60 + "\n")
    
    # Initialize generator
    generator = ChangelogGenerator(".")
    
    # Load all versions
    generator.load_versions()
    
    if not generator.versions:
        print("❌ No version files found!")
        return
    
    # Print summary
    generator.print_summary()
    
    # Generate and save changelog
    output_file = generator.save_changelog()
    
    print(f"\n✨ Done! Check out {output_file} for the full changelog.")
    print("💡 Tip: Also check CHANGELOG_COMPACT.md for a quick overview.\n")


if __name__ == "__main__":
    main()