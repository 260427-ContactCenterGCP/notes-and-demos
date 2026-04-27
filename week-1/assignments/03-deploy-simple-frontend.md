# Assignment 3: Deploy a Personal Static Website on GCP

## Objective
Create and deploy a personal website using HTML, CSS, and JavaScript (or TypeScript) on Google Cloud Platform.

The website should include:
- Your name
- Short bio
- At least 3 fun facts
- A picture
- Basic styling and interactivity

---

## Cloud Storage Static Website Hosting

---

# 1. Create a Cloud Storage Bucket

Go to **Cloud Storage → Buckets → Create**

Configuration:
- Bucket name: must be globally unique (e.g. my-name-website-123)
- Location: choose nearest region
- Storage class: Standard

Click Create

---

# 2. Upload Website Files

Upload the following files:
- index.html
- styles.css
- script.js
- image file (jpg/png)

---

# 3. Make Files Public

Go to Permissions → Grant Access

Add:
- Principal: allUsers
- Role: Storage Object Viewer

This makes the site publicly accessible.

---

# 4. Enable Static Website Hosting

In bucket settings:
- Set Main Page: index.html
- (Optional) Error Page: 404.html

---

# 5. Access Website

Open the public bucket URL provided by GCP.

---

## Example Website Structure

### index.html
<!DOCTYPE html>
<html>
<head>
  <title>My Website</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Your Name</h1>

  <p>Short bio goes here.</p>

  <h2>Fun Facts</h2>
  <ul>
    <li>Fun fact 1</li>
    <li>Fun fact 2</li>
    <li>Fun fact 3</li>
  </ul>

  <img src="me.jpg" width="200">

  <script src="script.js"></script>
</body>
</html>

---

### styles.css
body {
  font-family: Arial;
  text-align: center;
}

---

### script.js
console.log("Website loaded!");

---

## Deliverables
- Live website URL
- Screenshot of website
- Source code files

---

## Bonus Challenges
- Connect to your Compute Engine instance and fetch some of the data from there

---

## Notes
- Ensure bucket is public for access
- Avoid uploading sensitive files
