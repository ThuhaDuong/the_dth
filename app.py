from flask import Flask, render_template_string, send_from_directory
import os
import json

# Creating a Flask app - this basically starts up a web server
app = Flask(__name__)

# This lets the browser access images from the assets folder
# Without this, your images won't load on the webpage
@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename)

# My wardrobe, listed as a dictionary in Python
# Each category has a list of tuples: (item_name, image_path)
# You can add more items here, just follow the same format!
wardrobe = {
    "tops": [
        ("Hollister Hoodie", "/assets/hoodie.png"),
        ("Grey Sweater", "/assets/grey-knit-sweater.png"),
        ("Radiohead Tshirt", "/assets/band_t-shirt.png")    
    ],
    "bottoms": [
        ("Black Mini Skirt", "/assets/mini_dress.png"),
        ("Jeans", "/assets/jeans_1.png"),
        ("Tracksuit Pants", "/assets/tracksuit_pant.png")
    ],
    "shoes": [
        ("Brown Boots", "/assets/brown_boots.png"),
        ("Blue Converse", "/assets/blue_converse.png"),
        ("Brown Oxford Shoes", "/assets/brown_oxford.png")
    ]
}


# This is the main page that shows up when you go to http://127.0.0.1:5000
@app.route('/')
def index():
    """Render the digital closet HTML page with wardrobe data from Python."""
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Closet - Clueless Style</title>
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Crect fill='%235BCEFA' width='16' height='3.2'/%3E%3Crect fill='%23F5A9B8' y='3.2' width='16' height='3.2'/%3E%3Crect fill='%23FFFFFF' y='6.4' width='16' height='3.2'/%3E%3Crect fill='%23F5A9B8' y='9.6' width='16' height='3.2'/%3E%3Crect fill='%235BCEFA' y='12.8' width='16' height='3.2'/%3E%3C/svg%3E">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            background: linear-gradient(135deg, #87CEEB 0%, #98D8E8 25%, #B0E0E6 50%, #AFEEEE 75%, #E0F6FF 100%);
            background-image: url("/assets/1349543.png");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-blend-mode: overlay;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            position: relative;
        }

        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 20% 50%, rgba(135, 206, 235, 0.3) 0%, transparent 50%),
                        radial-gradient(circle at 80% 80%, rgba(176, 224, 230, 0.3) 0%, transparent 50%);
            pointer-events: none;
            z-index: 0;
        }

        .container {
            background: rgba(255, 255, 255, 0.6);
            border-radius: 40px;
            padding: 40px;
            max-width: 700px;
            width: 100%;
            box-shadow: 0 15px 35px rgba(135, 206, 235, 0.4),
                        inset 0 1px 0 rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(255, 255, 255, 0.5);
            position: relative;
            z-index: 1;
        }

        h1 {
            text-align: center;
            background: linear-gradient(135deg, #39FF14 0%, #00FF7F 50%, #7FFF00 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 2.8em;
            margin-bottom: 40px;
            text-shadow: 0 0 30px rgba(57, 255, 20, 0.5);
            font-weight: bold;
            letter-spacing: 1px;
        }

        .category-section {
            margin-bottom: 35px;
            text-align: center;
            background: rgba(255, 255, 255, 0.4);
            border-radius: 25px;
            padding: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.6);
        }

        .category-title {
            font-size: 1.4em;
            color: #2C5F8D;
            margin-bottom: 15px;
            font-weight: 600;
            text-transform: none;
            letter-spacing: 1px;
            text-shadow: 0 2px 4px rgba(255, 255, 255, 0.8);
        }

        .item-selector {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }

        .nav-button {
            background: linear-gradient(135deg, #4A90E2 0%, #5FB3D3 100%);
            color: white;
            border: 2px solid rgba(255, 255, 255, 0.6);
            border-radius: 50%;
            width: 55px;
            height: 55px;
            font-size: 1.5em;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 6px 20px rgba(74, 144, 226, 0.4),
                        inset 0 1px 0 rgba(255, 255, 255, 0.5);
        }

        .nav-button:hover {
            background: linear-gradient(135deg, #5FB3D3 0%, #7FCDCD 100%);
            transform: scale(1.15) translateY(-2px);
            box-shadow: 0 8px 25px rgba(95, 179, 211, 0.5),
                        inset 0 1px 0 rgba(255, 255, 255, 0.7);
        }

        .nav-button:active {
            transform: scale(1.05);
        }

        .item-display {
            flex: 1;
            min-width: 200px;
            max-width: 250px;
        }

        .item-image {
            width: 100%;
            height: 200px;
            object-fit: contain;
            border-radius: 20px;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.8) 0%, rgba(240, 255, 255, 0.9) 100%);
            padding: 15px;
            box-shadow: 0 8px 20px rgba(74, 144, 226, 0.2),
                        inset 0 1px 0 rgba(255, 255, 255, 0.9);
            border: 2px solid rgba(255, 255, 255, 0.6);
            transition: all 0.3s ease;
        }

        .item-image:hover {
            transform: scale(1.08);
            box-shadow: 0 12px 30px rgba(74, 144, 226, 0.3),
                        inset 0 1px 0 rgba(255, 255, 255, 1);
        }

        .outfit-display {
            margin-top: 40px;
            padding: 25px;
            background: linear-gradient(135deg, rgba(135, 206, 235, 0.5) 0%, rgba(176, 224, 230, 0.5) 100%);
            border-radius: 25px;
            text-align: center;
            box-shadow: 0 6px 20px rgba(135, 206, 235, 0.3),
                        inset 0 1px 0 rgba(255, 255, 255, 0.7);
            border: 2px solid rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(10px);
        }

        .outfit-text {
            font-size: 1.3em;
            color: #2C5F8D;
            line-height: 1.8;
            font-weight: 500;
            text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
        }

        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }

            h1 {
                font-size: 2em;
            }

            .category-title {
                font-size: 1.2em;
            }

            .nav-button {
                width: 45px;
                height: 45px;
                font-size: 1.2em;
            }

            .item-image {
                height: 150px;
            }

            .outfit-text {
                font-size: 1.1em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🫦 Digital Closet 💅</h1>
        
        <div class="category-section">
            <div class="category-title">👕 Top</div>
            <div class="item-selector">
                <button class="nav-button" onclick="prevItem('tops')">◀</button>
                <div class="item-display">
                    <img id="top-image" class="item-image" src="" alt="Top item">
                </div>
                <button class="nav-button" onclick="nextItem('tops')">▶</button>
            </div>
        </div>

        <div class="category-section">
            <div class="category-title">👖 Bottom</div>
            <div class="item-selector">
                <button class="nav-button" onclick="prevItem('bottoms')">◀</button>
                <div class="item-display">
                    <img id="bottom-image" class="item-image" src="" alt="Bottom item">
                </div>
                <button class="nav-button" onclick="nextItem('bottoms')">▶</button>
            </div>
        </div>

        <div class="category-section">
            <div class="category-title">👟 Shoes</div>
            <div class="item-selector">
                <button class="nav-button" onclick="prevItem('shoes')">◀</button>
                <div class="item-display">
                    <img id="shoes-image" class="item-image" src="" alt="Shoes item">
                </div>
                <button class="nav-button" onclick="nextItem('shoes')">▶</button>
            </div>
        </div>

        <div class="outfit-display">
            <div class="outfit-text" id="outfit-text"></div>
        </div>
    </div>

    <script>
        // Wardrobe data from Python (this gets filled in by Flask)
        const wardrobe = {{ wardrobe_json | safe }};

        // Keep track of which item we're currently showing in each category
        // Starts at 0 (first item in each list)
        let indexes = {
            tops: 0,
            bottoms: 0,
            shoes: 0
        };

        // Updates all the images and text on the page
        function updateDisplay() {
            // Update the three images (top, bottom, shoes)
            // [0] is the name, [1] is the image path
            document.getElementById('top-image').src = wardrobe.tops[indexes.tops][1];
            document.getElementById('bottom-image').src = wardrobe.bottoms[indexes.bottoms][1];
            document.getElementById('shoes-image').src = wardrobe.shoes[indexes.shoes][1];

            // Update the outfit description text at the bottom
            const topName = wardrobe.tops[indexes.tops][0];
            const bottomName = wardrobe.bottoms[indexes.bottoms][0];
            const shoesName = wardrobe.shoes[indexes.shoes][0];
            
            document.getElementById('outfit-text').innerHTML = 
                `👕 ${topName} + 👖 ${bottomName} + 👟 ${shoesName}`;
        }

        // Clicking the "next" arrow button
        function nextItem(category) {
            // Move to next item, wrap around to 0 if we reach the end
            indexes[category] = (indexes[category] + 1) % wardrobe[category].length;
            updateDisplay();
        }

        // Clicking the "previous" arrow button
        function prevItem(category) {
            // Move to previous item, wrap around to last item if we go below 0
            indexes[category] = (indexes[category] - 1 + wardrobe[category].length) % wardrobe[category].length;
            updateDisplay();
        }

        // Show the first items when the page loads
        updateDisplay();
    </script>
</body>
</html>
    """
    
    # Convert the Python wardrobe dictionary to JSON so JavaScript can use it
    # JavaScript can't directly read Python, so we convert it to a format it understands
    wardrobe_json = json.dumps(wardrobe)
    
    # This sends the HTML page to your browser with the wardrobe data inserted
    return render_template_string(html_template, wardrobe_json=wardrobe_json)


# This runs the server when you execute the file (python app.py)
if __name__ == "__main__":
    # debug=False means it won't auto-reload on changes (set to True if you want that)
    # port=5000 is just the address number (localhost:5000)
    app.run(debug=False, port=5000)

