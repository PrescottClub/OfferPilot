# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

OfferPilot is a WeChat Mini Program designed to help users with their study abroad applications. It provides tools for IELTS speaking practice, document editing, Q&A community, visa guidance, interview preparation, and university database access.

## Development Environment

This is a WeChat Mini Program that uses:
- WXML for view templates
- WXSS for stylesheets  
- JavaScript for logic
- WeChat DevTools for development and testing

## Common Commands

Since this is a WeChat Mini Program, development is primarily done through WeChat DevTools. No build scripts are currently configured in package.json.

To develop this project:
1. Open WeChat DevTools
2. Import the project directory
3. Use the preview and debugging features in WeChat DevTools

## Architecture

### Page Structure
The app follows the standard WeChat Mini Program structure with three main pages:

- `pages/tools/tools` - Main tools interface with search functionality for study abroad resources
- `pages/chat/chat` - AI chat interface for conversations
- `pages/profile/profile` - User profile management for personal information

### App Configuration
- `app.json` - Defines page routes, navigation bar styling, and tab bar configuration
- `project.config.json` - WeChat Mini Program project settings with ES6, PostCSS, and minification enabled
- App ID: wxf3c2565e0e00d81a

### Key Features
- Bottom tab navigation with three sections: 工具栏 (Tools), 对话 (Chat), 我的信息 (Profile)
- Tools page includes searchable grid of study abroad utilities (IELTS practice, document editing, etc.)
- Profile section for managing application information (target regions, language scores, universities, majors)

### File Organization
Each page follows WeChat Mini Program conventions:
- `.js` - Page logic and data handling
- `.wxml` - Page template structure
- `.wxss` - Page-specific styles
- `.json` - Page configuration

The tools page implements search functionality filtering through available study abroad tools based on user input.