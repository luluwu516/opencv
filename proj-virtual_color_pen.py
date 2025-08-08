import cv2
import numpy as np

class VirtualColorPen:
    """
    Virtual Color Pen application that tracks colored objects and draws trails
    """
    
    def __init__(self):
        # HSV color ranges for pen detection [h_min, s_min, v_min, h_max, s_max, v_max]
        self.detected_color_hsv = {
            'red': [0, 88, 125, 4, 255, 255],
            'blue': [90, 62, 125, 120, 255, 255]
        }
        
        # BGR color values for drawing
        self.pen_color_bgr = {
            'red': [0, 0, 255],
            'blue': [255, 0, 0]
        }
        
        # Store drawing points as [x, y, color_name]
        self.drawing_points = []
        
        # Minimum contour area threshold to filter noise
        self.min_contour_area = 700
        
        # Circle radius for pen tip and drawing
        self.pen_radius = 10
    
    def find_pen_positions(self, frame, canvas):
        """
        Detect colored objects in the frame and mark their positions
        
        Args:
            frame: Original camera frame
            canvas: Canvas to draw on
        """
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        for color_name, hsv_range in self.detected_color_hsv.items():
            lower = np.array(hsv_range[:3])
            upper = np.array(hsv_range[3:6])
            
            mask = cv2.inRange(hsv, lower, upper)
            
            # Find pen position from the mask
            pen_x, pen_y = self._find_contour_center(mask)
            
            # if pen is detected, draw indicator and add to drawing points
            if pen_y != -1:
                # Draw current pen position indicator
                cv2.circle(canvas, (pen_x, pen_y), self.pen_radius, 
                          self.pen_color_bgr[color_name], cv2.FILLED)
                
                # Add point to drawing history
                self.drawing_points.append([pen_x, pen_y, color_name])
    
    def _find_contour_center(self, mask):
        """
        Find the center point of the largest contour in the mask
        
        Args:
            mask: Binary mask image
            
        Returns:
            tuple: (center_x, center_y) or (-1, -1) if no valid contour found
        """
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Initialize return values
        center_x, center_y = -1, -1
        
        for contour in contours:
            area = cv2.contourArea(contour)
            
            if area > self.min_contour_area:
                x, y, w, h = cv2.boundingRect(contour)
                
                # Calculate center point (top-center for pen tip effect)
                center_x = x + (w // 2)
                center_y = y
                
                break  # use the first (largest) valid contour
        
        return center_x, center_y
    
    def draw_trail(self, canvas):
        """
        Draw all the points in the drawing history to create a trail effect
        
        Args:
            canvas: Canvas to draw the trail on
        """
        for point in self.drawing_points:
            x, y, color_name = point[0], point[1], point[2]
            cv2.circle(canvas, (x, y), self.pen_radius, 
                      self.pen_color_bgr[color_name], cv2.FILLED)
    
    def clear_drawing(self):
        """
        Clear all drawing points
        """
        self.drawing_points.clear()
    
    def run(self):
        """
        Main application loop
        """
        cap = cv2.VideoCapture(0)
        
        # Check if camera is accessible
        if not cap.isOpened():
            print("Error: Could not open camera")
            return
        
        print("Virtual Color Pen Started!")
        print("Controls:")
        print("  'q' - Quit application")
        print("  'c' - Clear drawing")
        print("  Show red or blue objects to the camera to draw")
        
        try:
            while True:
                ret, frame = cap.read()
                
                if not ret:
                    print("Error: Failed to read from camera")
                    break
                
                canvas = frame.copy()
                
                # Flip frame horizontally for mirror effect (more intuitive)
                frame = cv2.flip(frame, 1)
                canvas = cv2.flip(canvas, 1)
                
                self.find_pen_positions(frame, canvas)
                self.draw_trail(canvas)
                
                cv2.imshow("Virtual Color Pen", canvas)
                
                # Handle key presses
                key = cv2.waitKey(1) & 0xFF  # ensures ord('q') comparison works consistently across different operating systems
                if key == ord('q'):
                    break
                elif key == ord('c'):
                    self.clear_drawing()
                    print("Drawing cleared!")
        
        except KeyboardInterrupt:
            print("\nApplication interrupted by user")
        
        finally:
            # Clean up resources
            cap.release()
            cv2.destroyAllWindows()
            print("Virtual Color Pen closed")

def main():
    """
    Entry point of the application
    """
    pen_app = VirtualColorPen()
    pen_app.run()

if __name__ == "__main__":
    main()