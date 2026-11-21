
from flask import Flask, render_template, request

app = Flask(__name__)

# Job Dataset using List and Dictionaries
jobs = [
    {
        "title": "Python Developer",
        "company": "Tech Solutions",
        "skills": ["python", "oop", "sql", "git"]
    },
    {
        "title": "Web Developer",
        "company": "Creative Technologies",
        "skills": ["html", "css", "javascript", "python"]
    },
    {
        "title": "Data Analyst",
        "company": "Data Insights",
        "skills": ["python", "sql", "excel", "statistics"]
    },
    {
        "title": "Frontend Developer",
        "company": "Digital Studio",
        "skills": ["html", "css", "javascript", "react"]
    },
    {
        "title": "Database Administrator",
        "company": "IT Experts",
        "skills": ["sql", "database", "mysql", "python"]
    },
    {
        "title": "Software Engineer",
        "company": "SoftTech",
        "skills": ["python", "oop", "dsa", "git"]
    }
]


@app.route("/", methods=["GET", "POST"])
def home():

    results = []
    user_skills = ""
    error = ""

    if request.method == "POST":

        user_skills = request.form.get("skills", "").strip()

        if not user_skills:
            error = "Please enter at least one skill."

        else:
            # Convert input into a Set
            user_skill_set = {
                skill.strip().lower()
                for skill in user_skills.split(",")
                if skill.strip()
            }

            if not user_skill_set:
                error = "Please enter valid skills separated by commas."

            else:
                # Search and calculate matching percentage
                for job in jobs:

                    required_skills = set(job["skills"])

                    matching_skills = (
                        user_skill_set.intersection(required_skills)
                    )

                    percentage = (
                        len(matching_skills) /
                        len(required_skills)
                    ) * 100

                    results.append({
                        "title": job["title"],
                        "company": job["company"],
                        "skills": job["skills"],
                        "matched": sorted(matching_skills),
                        "percentage": round(percentage, 2)
                    })

                # Sort by highest match percentage
                results.sort(
                    key=lambda job: job["percentage"],
                    reverse=True
                )

    return render_template(
        "index.html",
        results=results,
        user_skills=user_skills,
        searched=request.method == "POST",
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
