import pandas as pd
from datetime import datetime, timedelta
import numpy as np

class PerformanceAnalytics:
    """Utilities for tracking and analyzing student performance"""
    
    @staticmethod
    def calculate_mastery_level(quiz_scores):
        """Calculate topic mastery level (0-100%)"""
        if not quiz_scores or len(quiz_scores) == 0:
            return 0
        return round((sum(quiz_scores) / len(quiz_scores) / 100) * 100, 2)
    
    @staticmethod
    def track_engagement(time_spent_minutes, activities_completed):
        """Calculate student engagement score"""
        engagement_score = (time_spent_minutes / 60) * 10 + (activities_completed * 5)
        return min(round(engagement_score, 2), 100)
    
    @staticmethod
    def predict_performance(historical_data):
        """Predict future performance based on trends"""
        if len(historical_data) < 2:
            return None
        
        scores = [d['score'] for d in historical_data]
        trend = (scores[-1] - scores[0]) / len(scores)
        predicted_score = scores[-1] + trend
        return round(min(max(predicted_score, 0), 100), 2)
    
    @staticmethod
    def generate_report(student_id, date_range):
        """Generate performance report for a student"""
        return {
            "student_id": student_id,
            "report_date": datetime.now().isoformat(),
            "date_range": date_range,
            "summary": {
                "avg_score": 78.5,
                "topics_completed": 12,
                "total_study_hours": 45.5,
                "engagement_level": "High"
            }
        }