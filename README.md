# Mini Teams

Mini Teams is a simple web-based chat application that allows users to join different teams and send real-time messages using WebSockets. Built with **FastAPI** for the backend and **Vanilla JavaScript** for the frontend.

## Features

- **Real-time Messaging**: Users can join a team and send messages that are broadcast to all team members.
- **WebSocket Connection**: Establishes a full-duplex communication channel between the frontend and backend.
- **Multiple Teams**: Users can create or join different teams to chat in isolated channels.

## Tech Stack
- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript
- **WebSockets**: For real-time communication
- **Database**: None (For simplicity, messages are not stored)
- **Deployment**: Temporary public access via **ngrok**

## Setup Instructions

### Prerequisites
- Python 3.x
- `pip` (for installing Python dependencies)
- [ngrok](https://ngrok.com/) for public access (if you don’t have it installed, follow their [installation guide](https://ngrok.com/download)).

### Steps to Run Locally

1. **Clone the repository**

   git clone https://github.com/<your-username>/Mini_Teams.git
   cd Mini_Teams
   
2. **Install dependencies**
    For python(backend)
    pip install -r requirements.txt
3.  **Run the FastAPI server**
    To start the backend locally, use the following command:
    uvicorn main:app --reload
4. **Expose your server using ngrok**
    If you don’t have ngrok installed, follow their installation instructions.
    Then, expose the FastAPI server using ngrok:
    **ngrok http 8000**
    this will generate a public url
5. Access the app in the browser



   
