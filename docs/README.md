# Python Practice Questions - Web Platform

## Features

✅ **Interactive Python Editor** - Write and run Python code directly in your browser using PyScript  
✅ **Progress Tracking** - Track your progress with localStorage (syncs across sessions)  
✅ **1000 Questions** - Organized across 6 difficulty levels  
✅ **Achievements System** - Unlock badges as you progress  
✅ **Streak Tracking** - Maintain your learning streak  
✅ **Beautiful Dashboard** - Visualize your learning journey  

## Quick Start

1. Visit the GitHub Pages site: `https://pavanmudigondatr.github.io/python-bro-code/`
2. Click "Code Editor" to start practicing
3. Write Python code in the editor
4. Click "Run Code" to see results
5. Mark questions as complete to track progress

## How It Works

- **PyScript**: Runs Python code in WebAssembly in your browser (no server needed!)
- **LocalStorage**: Saves your progress locally in your browser
- **GitHub Pages**: Hosts the static site for free
- **Responsive Design**: Works on desktop, tablet, and mobile

## Progress Data

Your progress is stored locally in your browser using localStorage. To backup or transfer progress:

1. Open browser console (F12)
2. Run: `console.log(progressTracker.exportProgress())`
3. Copy the JSON output
4. To restore: `progressTracker.importProgress(jsonString)`

## Offline Support

After first visit, the site works offline thanks to browser caching.

## Technologies Used

- HTML5 / CSS3
- JavaScript (ES6+)
- PyScript (Python in WebAssembly)
- Font Awesome Icons
- LocalStorage API

## Browser Compatibility

- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support  
- Safari: ✅ Full support
- Mobile browsers: ✅ Responsive design

## Privacy

All data is stored locally in your browser. Nothing is sent to any server.

## License

Open source - free to use and modify
