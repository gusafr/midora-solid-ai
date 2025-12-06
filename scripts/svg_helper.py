"""
SVG to ReportLab Integration Helper

Converts SVG diagrams to ReportLab Drawing objects for PDF embedding.
Requires: pip install svglib reportlab
"""

import os
from pathlib import Path
from typing import Optional, Tuple
from reportlab.platypus import Image, Flowable
from reportlab.lib.units import cm

try:
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPDF
    SVGLIB_AVAILABLE = True
except ImportError:
    SVGLIB_AVAILABLE = False


class SVGDiagram(Flowable):
    """Custom Flowable to embed SVG diagrams in PDF."""
    
    def __init__(self, svg_path: str, width: float = 15*cm, height: float = None):
        """
        Initialize SVG diagram flowable.
        
        Args:
            svg_path: Path to SVG file
            width: Desired width in ReportLab units (default 15cm)
            height: Desired height in ReportLab units (None = auto-scale)
        """
        Flowable.__init__(self)
        self.svg_path = svg_path
        self.drawing = None
        self.desired_width = width
        self.desired_height = height
        
        # Load SVG
        if SVGLIB_AVAILABLE and os.path.exists(svg_path):
            try:
                self.drawing = svg2rlg(svg_path)
                if self.drawing:
                    # Calculate scaling
                    scale_w = width / self.drawing.width if self.drawing.width > 0 else 1
                    if height:
                        scale_h = height / self.drawing.height if self.drawing.height > 0 else 1
                        scale = min(scale_w, scale_h)
                    else:
                        scale = scale_w
                    
                    # Apply scaling
                    self.drawing.width = self.drawing.width * scale
                    self.drawing.height = self.drawing.height * scale
                    self.drawing.scale(scale, scale)
                    
                    # Set flowable dimensions
                    self.width = self.drawing.width
                    self.height = self.drawing.height
                else:
                    self.width = width
                    self.height = height or (width * 0.6)  # Default aspect ratio
            except Exception as e:
                print(f"⚠️ Warning: Could not load SVG {svg_path}: {e}")
                self.drawing = None
                self.width = width
                self.height = height or (width * 0.6)
        else:
            self.width = width
            self.height = height or (width * 0.6)
    
    def draw(self):
        """Render the SVG diagram on the canvas."""
        if self.drawing:
            try:
                renderPDF.draw(self.drawing, self.canv, 0, 0)
            except ValueError as e:
                # Handle SVG rendering errors (e.g., invalid dash patterns)
                if 'setDash' in str(e):
                    # Fallback: Draw placeholder box with error message
                    self._draw_placeholder(f"SVG rendering error (dash pattern)")
                else:
                    raise
            except Exception as e:
                # Fallback for any other rendering errors
                self._draw_placeholder(f"SVG rendering error: {str(e)[:50]}")
        else:
            # Fallback: Draw placeholder box
            self._draw_placeholder(f"SVG diagram: {Path(self.svg_path).name}")
    
    def _draw_placeholder(self, text: str):
        """Draw a placeholder box when SVG rendering fails."""
        self.canv.saveState()
        self.canv.setStrokeColorRGB(0.8, 0.8, 0.8)
        self.canv.setFillColorRGB(0.95, 0.95, 0.95)
        self.canv.rect(0, 0, self.width, self.height, fill=1)
        
        # Add text
        self.canv.setFillColorRGB(0.4, 0.4, 0.4)
        self.canv.setFont("Helvetica", 10)
        text_width = self.canv.stringWidth(text, "Helvetica", 10)
        self.canv.drawString((self.width - text_width) / 2, 
                            self.height / 2, text)
        self.canv.restoreState()


def find_svg_for_diagram(diagram_path: str, diagrams_dir: Path) -> Optional[Path]:
    """
    Find corresponding image file for a .mmd diagram reference.
    Prefers PNG over SVG for more reliable PDF rendering.
    
    Args:
        diagram_path: Path from markdown (e.g., "DIAGRAMS/ai-native-safe-model.mmd")
        diagrams_dir: Root diagrams directory
        
    Returns:
        Path to image file if found, None otherwise
    """
    # Extract base filename (without .mmd extension)
    if diagram_path.endswith('.mmd'):
        base_name = Path(diagram_path).stem
    else:
        base_name = Path(diagram_path).name
    
    # Try PNG first (more reliable rendering in ReportLab)
    png_path = diagrams_dir / "images" / "png" / f"{base_name}.png"
    if png_path.exists():
        return png_path
    
    # Try SVG as fallback
    svg_path = diagrams_dir / "images" / "svg" / f"{base_name}.svg"
    if svg_path.exists():
        return svg_path
    
    return None


def create_diagram_flowable(diagram_path: str, 
                            diagrams_dir: Path,
                            width: float = 15*cm,
                            height: float = None) -> Tuple[Optional[Flowable], str]:
    """
    Create a flowable for a diagram (PNG preferred, SVG fallback).
    
    Args:
        diagram_path: Path from markdown (e.g., "DIAGRAMS/ai-native-safe-model.mmd")
        diagrams_dir: Root diagrams directory
        width: Desired width
        height: Desired height (None = auto)
        
    Returns:
        Tuple of (flowable, diagram_name) or (None, diagram_name) if not found
    """
    # Extract diagram name for display
    base_name = Path(diagram_path).stem if diagram_path.endswith('.mmd') else Path(diagram_path).name
    diagram_name = base_name.replace('-', ' ').replace('_', ' ').title()
    
    # Find image file (PNG preferred)
    image_path = find_svg_for_diagram(diagram_path, diagrams_dir)
    
    if not image_path:
        return None, diagram_name
    
    # Create appropriate flowable
    # Always use Image for both PNG and SVG (more reliable)
    if image_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
        # For raster images, constrain to page width and reasonable height
        from PIL import Image as PILImage
        try:
            with PILImage.open(str(image_path)) as img:
                aspect_ratio = img.height / img.width
                calc_height = width * aspect_ratio
                # Limit height to avoid page overflow (max 16cm ~= 6 inches)
                max_height = 16*cm
                if calc_height > max_height:
                    calc_height = max_height
                    width = max_height / aspect_ratio
                return Image(str(image_path), width=width, height=calc_height), diagram_name
        except:
            # Fallback: Let ReportLab auto-calculate, but this might fail
            return Image(str(image_path), width=width), diagram_name
    elif image_path.suffix.lower() == '.svg':
        # For SVG, try using Image class first (works in newer ReportLab)
        try:
            return Image(str(image_path), width=width), diagram_name
        except:
            # Fallback to SVGDiagram if Image doesn't support SVG
            if SVGLIB_AVAILABLE:
                return SVGDiagram(str(image_path), width, height), diagram_name
            else:
                return None, diagram_name
    else:
        return None, diagram_name


def check_dependencies() -> bool:
    """
    Check if SVG dependencies are available.
    
    Returns:
        True if svglib is installed, False otherwise
    """
    return SVGLIB_AVAILABLE


def install_instructions() -> str:
    """
    Get installation instructions for SVG support.
    
    Returns:
        Installation command string
    """
    return "pip install svglib reportlab"
