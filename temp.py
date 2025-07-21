from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Load video
clip = VideoFileClip("/Users/arrryyy/Desktop/Projects/Reworked/Sales_KPI_dashboard/Data/Screen Recording 2025-07-21 at 14.02.36.mov").subclip(0, 10)

# Add top annotation
text = TextClip("Sales KPI Dashboard • Interactive Charts & KPI Tracking",
                fontsize=24, color='white', bg_color='black',
                size=(clip.w, 40)).set_position(("center", "top")).set_duration(clip.duration)

# Combine video and text
final_clip = CompositeVideoClip([clip, text])

# Export as GIF
final_clip.write_gif("sales_kpi_dashboard.gif", fps=10)