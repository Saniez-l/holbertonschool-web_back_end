const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;
const DB_FILE = process.argv.length > 2 ? process.argv[2] : '';

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  fs.readFile(DB_FILE, 'utf8', (err, data) => {
    const responseParts = ['This is the list of our students'];

    if (err) {
      responseParts.push('Cannot load the database');
      res.send(responseParts.join('\n'));
      return;
    }

    const lines = data.toString().split('\n').filter((line) => line.trim().length > 0);

    lines.shift();

    const fields = {};
    const students = lines;
    students.forEach((student) => {
      const info = student.split(',');
      if (info.length === 4) {
        const field = info[3];
        const firstName = info[0];

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }
    });

    responseParts.push(`Number of students: ${students.length}`);

    for (const [field, names] of Object.entries(fields)) {
      responseParts.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }

    res.send(responseParts.join('\n'));
  });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

module.exports = app;
