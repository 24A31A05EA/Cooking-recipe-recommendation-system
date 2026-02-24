import os
import pandas as pd
import re

# Load CSV
df = pd.read_csv("cuisines.csv")

# Image folder path (relative to HTML)
image_folder = "image_for_cuisines/data"

print("Current Folder:", os.getcwd())
print("Image Folder Exists:", os.path.exists(image_folder))

# Helper: extract words from recipe name
def get_words(name):
    name = str(name).lower()
    words = re.findall(r'\w+', name)  # extract alphanumeric words
    return words

# Find matching image
def find_image(recipe_name, image_url=None):
    recipe_words = get_words(recipe_name)
    
    for file in os.listdir(image_folder):
        file_lower = file.lower()
        # If any word in recipe name appears in filename, use this image
        if any(word in file_lower for word in recipe_words):
            return f"{image_folder}/{file}"  # relative path for HTML

    # Fallback to image_url from CSV
    if image_url and isinstance(image_url, str) and image_url.strip() != "":
        return image_url

    # Final fallback: placeholder
    return "https://via.placeholder.com/400x300?text=No+Image"

# Assign images for all recipes
df["image"] = df.apply(lambda row: find_image(row["name"], row.get("image_url")), axis=1)

# Save JSON
df.to_json("recipes.json", orient="records", indent=4)

print("✅ JSON Updated Successfully!")

im using this and 
document.addEventListener("DOMContentLoaded", function () {

    const recipeName = localStorage.getItem("selectedRecipe");
    console.log("Selected recipe:", recipeName);

    fetch("recipes.json")
        .then(response => response.json())
        .then(data => {

            // Find recipe (case-insensitive safe match)
            const recipe = data.find(r =>
                r.name.trim().toLowerCase() === recipeName.trim().toLowerCase()
            );

            const container = document.getElementById("detailsContainer");

            if (!recipe) {
                container.innerHTML = "<h2>Recipe not found.</h2>";
                return;
            }

            // updated part
            container.innerHTML = `
                <div class="detail-page">

                    <div class="detail-title-box">
                        <h1>${recipe.name}</h1>
                        <div class="time-badge">
                            ⏱ ${recipe.prep_time} mins
                        </div>
                    </div>

                    <div class="detail-image-box">
                        <img src="https://source.unsplash.com/400x300/?${recipe.cuisine || 'food'}" alt="${recipe.name}">
                    </div>

                    <div class="detail-grid">

                        <div class="detail-box">
                            <h2>Description</h2>
                            <p>${recipe.description}</p>
                        </div>

                        <div class="detail-box">
                            <h2>Ingredients</h2>
                            <ul>
                                ${recipe.ingredients.map(item => `<li>${item}</li>`).join("")}
                            </ul>
                        </div>

                        <div class="detail-box full-width">
                            <h2>Preparation Steps</h2>
                            <ul>
                                ${
                                    recipe.instructions
                                        .split(".")
                                        .map(step => step.trim())
                                        .filter(step => step.length > 0)
                                        .map(step => `<li>${step}.</li>`)
                                        .join("")
                                }
                            </ul>
                        </div>

                    </div>

                    <div class="detail-footer">
                        <button onclick="goBack()">← Back</button>
                    </div>

                </div>
            `;
        })
        .catch(error => {
            console.error("Error loading details:", error);
        });

});

function goBack() {
    window.location.href = "recipes.html?from=details";
}

