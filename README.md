# FlexBook Frontend 📅

A modern, user-friendly web interface for the **FlexBook API** built with Streamlit. This frontend provides comprehensive venue and booking management capabilities with role-based authentication.

## 🌐 Live Demo

- **🚀 Frontend Application**: https://flexbook-on.streamlit.app/
- **📖 Backend API Docs**: https://flexbook-backend.onrender.com/docs

## ✨ Features

### 🔐 Authentication & Security
- User **signup** and **login** with JWT token management
- Session persistence for seamless user experience
- **Admin panel** for role management (`user`, `owner`, `admin`)

### 👤 User Management
- View all users (Admin only)
- Profile management (view, update, delete accounts)
- Role-based access control

### 🏢 Venue Management
- Browse all available venues
- Search venues by ID
- Create, update, and delete venues (`owner` and `admin` roles)
- Comprehensive venue details and availability

### 📅 Booking Management
- Create bookings for available venues
- View all bookings (Admin only)
- Manage personal bookings (view, update, cancel)
- Real-time availability checking

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Core web application framework |
| **Requests** | HTTP client for API communication |
| **PyJWT** | JWT token decoding and user info display |

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- FlexBook Backend API instance running

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/An-Array/FlexBook--frontend.git
   cd FlexBook--frontend
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the application**
   
   Create the Streamlit secrets configuration:
   ```bash
   mkdir .streamlit
   touch .streamlit/secrets.toml
   ```
   
   Add your backend API URL to `.streamlit/secrets.toml`:
   ```toml
   # .streamlit/secrets.toml
   BASE_URL = "http://127.0.0.1:8000"
   ```
   
   > **Note**: For local development, use `http://127.0.0.1:8000` as the default backend URL.

5. **Run the application**
   ```bash
   streamlit run app.py
   ```
   
   The application will be available at `http://localhost:8501`

## 🕹️ Usage Guide

1. **Start** by navigating to the **Auth** page via the sidebar
2. **Sign up** for a new account or **log in** with existing credentials
3. Once authenticated, your **User ID** and **Role** will be displayed
4. **Navigate** between management pages using the sidebar menu
5. **Select actions** from dropdown menus on each page (e.g., "Create Booking", "Get All Users")

### Demo Accounts

Test the application with these pre-configured accounts:

| Role | Email | Password |
|------|--------|----------|
| **Admin** | `admin@admin.com` | `admin` |
| **Owner** | `owner@owner.com` | `owner` |
| **User** | `user@user.com` | `user` |

## 🏗️ Project Structure

```
FlexBook--frontend/
├── .streamlit/
│   └── secrets.toml      # Backend URL configuration (gitignored)
├── pages/
│   ├── auth.py           # Authentication & admin panel
│   ├── users.py          # User management interface
│   ├── venues.py         # Venue management interface
│   └── bookings.py       # Booking management interface
├── app.py                # Main application & navigation
├── config.py             # Configuration & auth utilities
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🔗 Related Projects

- [FlexBook Backend API](https://github.com/An-Array/FlexBook-backend) - The REST API powering this frontend

---

*Built with ❤️ using Streamlit*