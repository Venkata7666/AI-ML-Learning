import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng(42)
study_hours = rng.uniform(1, 10, size=50)
exam_scores = 45 + 5 * study_hours + rng.normal(0, 5, size=50)

plt.figure(figsize=(8, 5))
plt.scatter(study_hours, exam_scores, color="steelblue", edgecolors="black", alpha=0.8)
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
