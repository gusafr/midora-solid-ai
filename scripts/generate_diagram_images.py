#!/usr/bin/env python3
"""
Generate SVG/PNG images from Mermaid diagrams

Usage:
    python scripts/generate_diagram_images.py
    python scripts/generate_diagram_images.py --format png --width 2400
"""

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional
import argparse


class DiagramImageGenerator:
    """Convert Mermaid .mmd files to SVG/PNG images."""
    
    def __init__(self, diagrams_dir: str = "DIAGRAMS",
                 output_dir: str = "DIAGRAMS/images",
                 format: str = "svg",
                 width: int = 1920,
                 height: int = 0,
                 background: str = "white",
                 theme: str = "default",
                 skip_existing: bool = False):
        self.diagrams_dir = Path(diagrams_dir)
        self.output_dir = Path(output_dir)
        self.format = format
        self.width = width
        self.height = height
        self.background = background
        self.theme = theme
        self.skip_existing = skip_existing
        
        self.total_converted = 0
        self.total_skipped = 0
        self.total_failed = 0
        
    def check_mermaid_cli(self) -> Optional[str]:
        """Check if Mermaid CLI is available."""
        print("ℹ️  Checking for Mermaid CLI...")
        
        # Check for mmdc globally
        try:
            result = subprocess.run(['mmdc', '--version'], 
                                  capture_output=True, text=True, check=False,
                                  timeout=5)
            if result.returncode == 0:
                version = result.stdout.strip()
                print(f"✅ Found Mermaid CLI: {version}")
                return "mmdc"
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
        
        # Check for npx
        try:
            # On Windows, npx might be npx.cmd or npx.ps1
            npx_cmd = 'npx' if sys.platform != 'win32' else 'npx.cmd'
            result = subprocess.run([npx_cmd, '--version'], 
                                  capture_output=True, text=True, check=False,
                                  timeout=5)
            if result.returncode == 0:
                print("⚠️  Mermaid CLI not installed globally, will use npx")
                print("ℹ️  Note: First run will download Mermaid CLI (may take a moment)")
                return "npx"
        except (FileNotFoundError, subprocess.TimeoutExpired):
            # Try plain 'npx' on Windows as fallback
            if sys.platform == 'win32':
                try:
                    result = subprocess.run(['npx', '--version'], 
                                          capture_output=True, text=True, check=False,
                                          timeout=5,
                                          shell=True)
                    if result.returncode == 0:
                        print("⚠️  Mermaid CLI not installed globally, will use npx")
                        print("ℹ️  Note: First run will download Mermaid CLI (may take a moment)")
                        return "npx"
                except:
                    pass
        
        print("❌ Mermaid CLI not found!")
        print("\nPlease install Mermaid CLI:")
        print("  Option 1: npm install -g @mermaid-js/mermaid-cli")
        print("  Option 2: Install Node.js (includes npx)")
        return None
    
    def clean_mermaid_content(self, content: str) -> str:
        """Remove code fences from Mermaid content."""
        # Remove ````plaintext```mermaid ... ``` ```` format
        match = re.search(r'````plaintext\s*```mermaid\s*([\s\S]*?)\s*```\s*````', 
                         content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        
        # Remove ```mermaid ... ``` format
        match = re.search(r'```mermaid\s*([\s\S]*?)\s*```', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        
        # Already clean
        return content.strip()
    
    def convert_diagram(self, mmd_file: Path, mermaid_cmd: str) -> bool:
        """Convert a single Mermaid diagram to image."""
        file_name = mmd_file.name
        output_subdir = self.output_dir / self.format
        output_file = output_subdir / f"{mmd_file.stem}.{self.format}"
        
        # Check if should skip
        if self.skip_existing and output_file.exists():
            print(f"⏭️  Skipping {file_name} (already exists)")
            self.total_skipped += 1
            return True
        
        print(f"ℹ️  Converting {file_name}...")
        
        try:
            # Read and clean content
            with open(mmd_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            cleaned_content = self.clean_mermaid_content(content)
            
            # Create temporary file with cleaned content
            with tempfile.NamedTemporaryFile(mode='w', suffix='.mmd', 
                                            delete=False, encoding='utf-8') as tmp:
                tmp.write(cleaned_content)
                tmp_path = tmp.name
            
            try:
                # Build command
                if mermaid_cmd == "mmdc":
                    cmd = ['mmdc']
                else:
                    # Use shell=True on Windows for npx
                    cmd = 'npx -y -p @mermaid-js/mermaid-cli mmdc'
                
                cmd_args = [
                    '-i', tmp_path,
                    '-o', str(output_file),
                    '-t', self.theme,
                    '-b', self.background
                ]
                
                if self.width > 0:
                    cmd_args.extend(['-w', str(self.width)])
                
                if self.height > 0:
                    cmd_args.extend(['-H', str(self.height)])
                
                # Execute conversion
                if isinstance(cmd, list):
                    cmd.extend(cmd_args)
                    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
                else:
                    # Build full command string for shell execution
                    full_cmd = f"{cmd} {' '.join(cmd_args)}"
                    result = subprocess.run(full_cmd, capture_output=True, text=True, 
                                          check=False, shell=True)
                
                if result.returncode == 0 and output_file.exists():
                    file_size_kb = output_file.stat().st_size / 1024
                    print(f"✅ ✓ {file_name} → {file_size_kb:.1f} KB")
                    self.total_converted += 1
                    return True
                else:
                    error_msg = result.stderr.strip() if result.stderr else "Unknown error"
                    print(f"❌ Conversion failed: {error_msg[:100]}")
                    self.total_failed += 1
                    return False
                    
            finally:
                # Clean up temp file
                try:
                    os.unlink(tmp_path)
                except:
                    pass
                    
        except Exception as e:
            print(f"❌ Error converting {file_name}: {e}")
            self.total_failed += 1
            return False
    
    def generate(self):
        """Generate all diagram images."""
        print()
        print("=" * 45)
        print("  Mermaid Diagram Image Generator")
        print("=" * 45)
        print()
        
        # Check prerequisites
        mermaid_cmd = self.check_mermaid_cli()
        if not mermaid_cmd:
            return 1
        
        # Validate input directory
        if not self.diagrams_dir.exists():
            print(f"❌ Diagrams directory not found: {self.diagrams_dir}")
            return 1
        
        # Find all .mmd files
        print(f"ℹ️  Scanning for .mmd files in {self.diagrams_dir}...")
        mmd_files = sorted(self.diagrams_dir.glob("*.mmd"))
        
        if not mmd_files:
            print(f"⚠️  No .mmd files found in {self.diagrams_dir}")
            return 0
        
        print(f"✅ Found {len(mmd_files)} diagram(s)")
        print()
        
        # Create output directory
        output_subdir = self.output_dir / self.format
        output_subdir.mkdir(parents=True, exist_ok=True)
        
        # Convert each diagram
        print(f"ℹ️  Converting diagrams to {self.format} format...")
        print(f"ℹ️  Output directory: {output_subdir}")
        print(f"ℹ️  Image size: {self.width}px width", end="")
        if self.height > 0:
            print(f" x {self.height}px height")
        else:
            print(" (auto height)")
        print(f"ℹ️  Theme: {self.theme} | Background: {self.background}")
        print()
        
        import time
        start_time = time.time()
        
        for mmd_file in mmd_files:
            self.convert_diagram(mmd_file, mermaid_cmd)
        
        duration = time.time() - start_time
        
        # Print summary
        print()
        print("=" * 45)
        print("  Conversion Complete")
        print("=" * 45)
        print()
        print("Statistics:")
        print(f"  ✅ Converted:  {self.total_converted}")
        print(f"  ⏭️  Skipped:    {self.total_skipped}")
        print(f"  ❌ Failed:     {self.total_failed}")
        print(f"  ⏱️  Duration:   {duration:.1f} seconds")
        print()
        
        if self.total_converted > 0:
            print(f"Output: {output_subdir}")
            
            # Calculate total size
            total_size = sum(f.stat().st_size for f in output_subdir.glob(f"*.{self.format}"))
            total_size_mb = total_size / (1024 * 1024)
            print(f"Total size: {total_size_mb:.2f} MB")
        
        print()
        
        # Create index file
        self.create_index(mmd_files)
        
        return 0 if self.total_failed == 0 else 1
    
    def create_index(self, mmd_files):
        """Create README index for generated images."""
        index_file = self.output_dir / "README.md"
        
        print(f"ℹ️  Generating image index: {index_file}")
        
        from datetime import datetime
        
        content = f"""# Diagram Images

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Format:** {self.format}  
**Source:** {self.diagrams_dir}  
**Total Diagrams:** {self.total_converted}

---

## Available Formats

- **SVG** - Scalable vector graphics (best for web, PDF, presentations)
- **PNG** - High-resolution raster images (universal compatibility)

---

## Diagrams

| # | Diagram | SVG | PNG | Source |
|---|---------|-----|-----|--------|
"""
        
        for i, mmd_file in enumerate(sorted(mmd_files), 1):
            name = mmd_file.stem
            title = name.replace('-', ' ').replace('_', ' ').title()
            
            svg_path = f"svg/{name}.svg"
            png_path = f"png/{name}.png"
            source_path = f"../{mmd_file.name}"
            
            svg_exists = (self.output_dir / svg_path).exists()
            png_exists = (self.output_dir / png_path).exists()
            
            svg_link = f"✅ [SVG]({svg_path})" if svg_exists else "❌"
            png_link = f"✅ [PNG]({png_path})" if png_exists else "❌"
            
            content += f"| {i} | **{title}** | {svg_link} | {png_link} | [.mmd]({source_path}) |\n"
        
        content += """

---

## Usage

### In PDF Generation (Python)
```python
from svg_helper import create_diagram_flowable

# Create flowable for diagram
flowable, name = create_diagram_flowable(
    'DIAGRAMS/ai-native-safe-model.mmd',
    diagrams_dir=Path('DIAGRAMS'),
    width=15*cm
)

# Add to PDF story
story.append(flowable)
```

### In Markdown Documentation
```markdown
![AI-Native SAFE Model](../DIAGRAMS/images/svg/ai-native-safe-model.svg)
```

### In Presentations
- Drag and drop SVG/PNG files into PowerPoint, Google Slides, etc.
- SVG files maintain quality at any zoom level
- PNG files work universally (fallback)

---

## Regeneration

```bash
# Generate SVG (default)
python scripts/generate_diagram_images.py

# Generate PNG (high-res)
python scripts/generate_diagram_images.py --format png --width 2400

# Skip existing files
python scripts/generate_diagram_images.py --skip-existing
```

---

**Last Updated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Index file created: {index_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate SVG/PNG images from Mermaid diagrams'
    )
    
    parser.add_argument(
        '--diagrams-dir',
        default='DIAGRAMS',
        help='Source directory with .mmd files (default: DIAGRAMS)'
    )
    parser.add_argument(
        '--output-dir',
        default='DIAGRAMS/images',
        help='Output directory (default: DIAGRAMS/images)'
    )
    parser.add_argument(
        '--format',
        choices=['svg', 'png', 'pdf'],
        default='svg',
        help='Output format (default: svg)'
    )
    parser.add_argument(
        '--width',
        type=int,
        default=1920,
        help='Image width in pixels (default: 1920)'
    )
    parser.add_argument(
        '--height',
        type=int,
        default=0,
        help='Image height in pixels, 0=auto (default: 0)'
    )
    parser.add_argument(
        '--background',
        default='white',
        help='Background color (default: white)'
    )
    parser.add_argument(
        '--theme',
        default='default',
        help='Mermaid theme (default: default)'
    )
    parser.add_argument(
        '--skip-existing',
        action='store_true',
        help='Skip files that already exist'
    )
    
    args = parser.parse_args()
    
    generator = DiagramImageGenerator(
        diagrams_dir=args.diagrams_dir,
        output_dir=args.output_dir,
        format=args.format,
        width=args.width,
        height=args.height,
        background=args.background,
        theme=args.theme,
        skip_existing=args.skip_existing
    )
    
    sys.exit(generator.generate())


if __name__ == '__main__':
    main()
