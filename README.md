# Digital Closet 🫦

A cute little web app inspired by the Clueless closet scene!

## What is this?

Basically, it's a website where you can browse through your wardrobe (tops, bottoms, shoes) and see outfit combinations. All the clothes data lives in a Python file, but you don't really need to touch that if you don't want to - you can just change the styling in the CSS section.

## Setting up

You'll need Python installed first. If you don't have it, download it from [python.org](https://www.python.org/downloads/).

1. **Install Flask** (this is what makes the website work):
   ```bash
   pip install -r requirements.txt
   ```
   
   If that doesn't work, try:
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Start the server**:
   ```bash
   python app.py
   ```
   
   Or if that doesn't work:
   ```bash
   python3 app.py
   ```

3. **Open your browser** and go to:
   ```
   http://127.0.0.1:5000
   ```

That's it! You should see your digital closet.

## Adding your own clothes

Open `app.py` and find the `wardrobe` dictionary (around line 17). It looks like this:

```python
wardrobe = {
    "tops": [
        ("Hollister Hoodie", "/assets/hoodie.png"),
        ("Grey Sweater", "/assets/grey-knit-sweater.png"),
        ...
    ],
    ...
}
```

To add a new item:
1. Put your image file in the `assets/` folder
2. Add a new line in the right category: `("Your Item Name", "/assets/your-image.png")`
3. Make sure the image path matches your filename exactly!

The format is always: `("Name", "/assets/filename.png")` - just copy one of the existing lines and change the name and filename.

## Customizing the design

All the CSS styling is in `app.py` too, inside the HTML template. Look for the `<style>` tag (around line 48). You can change:

- **Colors**: Search for color codes like `#4A90E2` (blue) or `#39FF14` (bright green)
- **Background image**: It's on line 58 - just change the filename
- **Fonts**: Line 56 has the font family
- **Sizes and spacing**: Most of the numbers are pretty self-explanatory if you play around with them

The CSS is all in one place, so it's easy to experiment. Just save the file and refresh your browser to see changes.

## Troubleshooting

**Images not showing?**
- Make sure your image files are actually in the `assets/` folder
- Check that the filenames match exactly (including .png vs .jpg)

**Port already in use?**
- Change `port=5000` to something else like `port=5001` at the bottom of `app.py`

**Can't install Flask?**
- Try `pip3` instead of `pip`
- On Mac or Linux, you might need `pip3 install --user Flask`

## Files you'll actually touch

- `app.py` - The main file with all the code (wardrobe list + HTML/CSS)
- `assets/` folder - Put all your clothing images here
- `requirements.txt` - Just has Flask in it

## Technologies used
- Flask web server: https://flask.palletsprojects.com/en/stable/quickstart/
- Python: https://docs.python.org/3/


