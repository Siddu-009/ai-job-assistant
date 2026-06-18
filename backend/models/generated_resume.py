from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class GeneratedResume(Base):
    __tablename__ = "generated_resumes"

    id = Column(Integer, primary_key=True, index=True)

    job_description = Column(Text)

    generated_resume = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
