from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

class AITutorChatbot:
    """AI-powered tutoring chatbot using DistilBERT"""
    
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")
        self.model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad")
        self.conversation_history = []
    
    def answer_question(self, question, context):
        """Answer student questions based on provided context"""
        inputs = self.tokenizer.encode_plus(question, context, return_tensors="pt")
        outputs = self.model(**inputs)
        start_idx = torch.argmax(outputs.start_logits)
        end_idx = torch.argmax(outputs.end_logits)
        answer = self.tokenizer.convert_tokens_to_string(
            self.tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start_idx:end_idx+1])
        )
        return answer
    
    def clarify_concept(self, concept, student_level):
        """Provide concept clarification based on student level"""
        clarifications = {
            "beginner": f"Simple explanation of {concept}",
            "intermediate": f"Detailed explanation of {concept}",
            "advanced": f"Advanced concepts related to {concept}"
        }
        return clarifications.get(student_level, "Concept explanation")
    
    def track_conversation(self, student_id, message, response):
        """Track conversation for analytics"""
        self.conversation_history.append({
            "student_id": student_id,
            "message": message,
            "response": response,
            "timestamp": datetime.now()
        })
