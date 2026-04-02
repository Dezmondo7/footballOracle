const express = require('express');
const cors = require('cors');
require('dotenv').config();
const { PythonShell } = require('python-shell');

const app = express();
app.use(cors());
app.use(express.json());

// The Oracle Route endpoint
app.get('/api/predict', (req, res) => {
    let options = {
        mode: 'text',
        pythonPath: 'C:\\Users\\user\\AppData\\Local\\Python\\bin\\python.exe', // Force it to use the standard python command
        pythonOptions: ['-u'], 
    };

    // This calls your Python script
    PythonShell.run('predict_logic.py', options).then(results => {
        res.json({
            status: "Success",
            match: "Bolton vs Portsmouth",
            prediction: results[0], // Grabs the 'print' from Python
            timestamp: new Date().toISOString()
        });
    }).catch(err => {
        res.status(500).json({ error: "Oracle is sleeping...", details: err.message });
    });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Oracle Engine humming on port ${PORT}`));