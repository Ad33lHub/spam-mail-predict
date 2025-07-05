# Spam Mail Prediction Project

## Overview
This project is a spam mail classifier that predicts whether an email is spam or not. It consists of a machine learning model trained on email data and a frontend interface built with Python to interact with the model.

## Project Structure
```
spam-mail-predict/
├── app/                  # Frontend application files
├── feature_extraction.pkl # Feature extraction pipeline
├── my_model.pkl          # Trained model file
├── rf_model.pkl          # Alternative trained model (Random Forest)
└── ...                   # Other project files
```

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.6 or higher
- Jupyter Notebook (for development/exploration)
- Required Python packages (install via `pip install -r requirements.txt`)

## Installation
1. Clone this repository:
   ```bash
   git clone [repository-url]
   cd spam-mail-predict
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Project
1. Navigate to the project directory:
   ```bash
   cd spam-mail-predict
   ```

2. Run the frontend application:
   ```bash
   python app/app.py
   ```

3. Open your web browser and go to:
   ```
   http://localhost:5000
   ```

## How It Works
1. The application loads the pre-trained model (`my_model.pkl` or `rf_model.pkl`) and feature extraction pipeline (`feature_extraction.pkl`).
2. When you enter an email text in the interface:
   - The text is processed using the same feature extraction pipeline used during training
   - The trained model makes a prediction (spam or not spam)
   - The result is displayed in the interface

## Tools and Technologies Used
- **Development Environment**: Jupyter Notebook
- **Machine Learning**: Scikit-learn
- **Frontend Framework**: Flask (Python web framework)
- **Feature Extraction**: TF-IDF Vectorizer (saved in `feature_extraction.pkl`)
- **Model**: Pre-trained classifier (saved in `my_model.pkl` and `rf_model.pkl`)

## File Descriptions
- `feature_extraction.pkl`: Serialized feature extraction pipeline
- `my_model.pkl`: Main trained model file
- `rf_model.pkl`: Alternative Random Forest model
- `app/`: Directory containing frontend application files
  - `app.py`: Main Flask application file
  - (other frontend files like templates, static files, etc.)

## Troubleshooting
If you encounter any issues:
- Ensure all required packages are installed
- Check that the model files are in the correct location
- Verify you're running the application from the root project directory

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
