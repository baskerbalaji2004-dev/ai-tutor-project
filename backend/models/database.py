# Database models

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    learning_paths = relationship('LearningPath', back_populates='user')

class LearningPath(Base):
    __tablename__ = 'learning_paths'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    topics = relationship('Topic', back_populates='learning_path')

class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    learning_path_id = Column(Integer, ForeignKey('learning_paths.id'))

class QuizResult(Base):
    __tablename__ = 'quiz_results'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    score = Column(Integer)

class ChatMessage(Base):
    __tablename__ = 'chat_messages'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String)

class AnalyticsData(Base):
    __tablename__ = 'analytics_data'
    id = Column(Integer, primary_key=True)
    learning_path_id = Column(Integer, ForeignKey('learning_paths.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    timestamp = Column(String)