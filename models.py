from datetime import datetime

class Business:
    # Initialize a new business with a name and category
    def __init__(self, name, category):
        self.name = name
        self.category = category
        # [span_7](start_span)[span_8](start_span)Requirement: Use datetime to timestamp entries[span_7](end_span)[span_8](end_span)
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Return the name in uppercase for the UI
    # [span_9](start_span)Requirement: A custom behavior method[span_9](end_span)
    def get_summary(self):
        return f"{self.name} ({self.category}) - Added on: {self.timestamp}"
    # NEW behavior method
    def get_styled_name(self):
       return self.name.upper()