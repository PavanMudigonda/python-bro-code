// Editor functionality
let currentQuestion = 1;
let currentLevel = 'beginner';
let startTime = null;
let questionsData = {}; // Will hold all 1000 questions

// Load questions data
async function initializeEditor() {
    try {
        const response = await fetch('data/questions.json');
        questionsData = await response.json();
        console.log('Loaded', Object.keys(questionsData).length, 'questions');
        
        // Now load the first question
        loadQuestion(currentQuestion);
    } catch (error) {
        console.error('Error loading questions:', error);
        // Fallback to default
        questionsData = {};
        // Still load the question with fallback data
        loadQuestion(currentQuestion);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Get level from URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('level')) {
        currentLevel = urlParams.get('level');
    }
    
    // Initialize editor and load questions
    initializeEditor();
    
    // Event listeners
    document.getElementById('run-code').addEventListener('click', runCode);
    document.getElementById('clear-code').addEventListener('click', clearCode);
    document.getElementById('save-code').addEventListener('click', saveCode);
    document.getElementById('mark-complete').addEventListener('click', markComplete);
    document.getElementById('prev-question').addEventListener('click', prevQuestion);
    document.getElementById('next-question').addEventListener('click', nextQuestion);
    document.getElementById('random-question').addEventListener('click', randomQuestion);
    document.getElementById('show-hints').addEventListener('click', toggleHints);
    document.getElementById('clear-output').addEventListener('click', clearOutput);
    
    // Track start time
    startTime = Date.now();
});

function runCode() {
    const code = document.getElementById('code-editor').value.trim();
    const outputDiv = document.getElementById('output');
    
    if (!code) {
        outputDiv.innerHTML = '<div class="output-info">Please write some code first</div>';
        return;
    }
    
    // Check if Skulpt is loaded
    if (typeof Sk === 'undefined') {
        outputDiv.innerHTML = '<div class="output-info">⏳ Python runtime is loading... Please wait a moment and try again.</div>';
        return;
    }
    
    // Run Python code using Skulpt
    window.runPythonCode(code);
}

function clearCode() {
    if (confirm('Clear all code? This cannot be undone.')) {
        document.getElementById('code-editor').value = '# Write your Python code here\n';
    }
}

function saveCode() {
    const code = document.getElementById('code-editor').value;
    const key = `code-${currentLevel}-${currentQuestion}`;
    localStorage.setItem(key, code);
    
    // Show success message
    const btn = document.getElementById('save-code');
    const originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-check"></i> Saved!';
    btn.style.background = '#28a745';
    
    setTimeout(() => {
        btn.innerHTML = originalText;
        btn.style.background = '';
    }, 2000);
}

function markComplete() {
    const endTime = Date.now();
    const timeTaken = Math.floor((endTime - startTime) / 1000); // seconds
    
    const success = progressTracker.markQuestionComplete(
        currentQuestion, 
        currentLevel, 
        timeTaken
    );
    
    if (success) {
        const message = document.getElementById('completion-message');
        message.style.display = 'block';
        
        setTimeout(() => {
            message.style.display = 'none';
            nextQuestion();
        }, 2000);
    } else {
        alert('Question already completed!');
    }
}

function loadQuestion(questionNum) {
    currentQuestion = questionNum;
    
    // Update UI
    document.getElementById('question-number').textContent = `Question ${String(questionNum).padStart(3, '0')}`;
    
    // Set difficulty badge
    const badge = document.getElementById('question-difficulty');
    if (questionNum <= 100) {
        currentLevel = 'beginner';
        badge.textContent = 'Beginner';
        badge.className = 'badge badge-beginner';
    } else if (questionNum <= 300) {
        currentLevel = 'intermediate';
        badge.textContent = 'Intermediate';
        badge.className = 'badge badge-intermediate';
    } else if (questionNum <= 500) {
        currentLevel = 'advanced';
        badge.textContent = 'Advanced';
        badge.className = 'badge badge-advanced';
    } else if (questionNum <= 700) {
        currentLevel = 'expert';
        badge.textContent = 'Expert';
        badge.className = 'badge badge-expert';
    } else if (questionNum <= 900) {
        currentLevel = 'master';
        badge.textContent = 'Master';
        badge.className = 'badge badge-master';
    } else {
        currentLevel = 'challenge';
        badge.textContent = 'Challenge';
        badge.className = 'badge badge-challenge';
    }
    
    // Load question content from JSON
    const questionData = questionsData[questionNum];
    if (questionData) {
        document.getElementById('question-title').textContent = questionData.title;
        
        // Build description HTML
        let descriptionHTML = `<p>${questionData.description}</p>`;
        if (questionData.example) {
            descriptionHTML += `<p><strong>Example:</strong></p><pre>${questionData.example}</pre>`;
        }
        document.getElementById('question-description').innerHTML = descriptionHTML;
        
        // Update hints
        if (questionData.hints && questionData.hints.length > 0) {
            let hintsHTML = '<ul>';
            questionData.hints.forEach(hint => {
                hintsHTML += `<li>${hint}</li>`;
            });
            hintsHTML += '</ul>';
            document.getElementById('hints-content').innerHTML = hintsHTML;
        }
        
        // Update meta info
        const metaHTML = `
            <div class="meta-item">
                <i class="fas fa-clock"></i>
                <span>Estimated: ${questionData.estimatedTime || 5} min</span>
            </div>
            <div class="meta-item">
                <i class="fas fa-tag"></i>
                <span>Tags: ${questionData.tags ? questionData.tags.join(', ') : 'practice'}</span>
            </div>
        `;
        document.querySelector('.question-meta').innerHTML = metaHTML;
    } else {
        // Fallback if question data not loaded
        document.getElementById('question-title').textContent = `Practice Question ${questionNum}`;
        document.getElementById('question-description').innerHTML = 
            `<p>Loading question details... If this persists, please refresh the page.</p>`;
    }
    
    // Load saved code if exists
    const savedCode = localStorage.getItem(`code-${currentLevel}-${questionNum}`);
    if (savedCode) {
        document.getElementById('code-editor').value = savedCode;
    } else {
        document.getElementById('code-editor').value = '# Write your Python code here\n';
    }
    
    // Clear output
    clearOutput();
    
    // Reset start time
    startTime = Date.now();
    
    // Hide completion message
    document.getElementById('completion-message').style.display = 'none';
    
    // Reset hints to hidden
    const hints = document.getElementById('hints-content');
    hints.classList.remove('visible');
    document.getElementById('show-hints').innerHTML = '<i class="fas fa-lightbulb"></i> Show Hints';
}

function prevQuestion() {
    if (currentQuestion > 1) {
        loadQuestion(currentQuestion - 1);
    }
}

function nextQuestion() {
    if (currentQuestion < 1000) {
        loadQuestion(currentQuestion + 1);
    }
}

function randomQuestion() {
    const random = Math.floor(Math.random() * 1000) + 1;
    loadQuestion(random);
}

function toggleHints() {
    const hints = document.getElementById('hints-content');
    hints.classList.toggle('visible');
    
    const btn = document.getElementById('show-hints');
    if (hints.classList.contains('visible')) {
        btn.innerHTML = '<i class="fas fa-eye-slash"></i> Hide Hints';
    } else {
        btn.innerHTML = '<i class="fas fa-lightbulb"></i> Show Hints';
    }
}

function clearOutput() {
    document.getElementById('output').innerHTML = 
        '<div class="output-placeholder">Click "Run Code" to see output here...</div>';
}
