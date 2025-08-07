document.addEventListener('DOMContentLoaded', () => {
  const captureBtn = document.getElementById('captureBtn');
  const submitBtn = document.getElementById('submitBtn');
  const videoUrlInput = document.getElementById('videoUrl');
  const notesResult = document.getElementById('notesResult');

  document.getElementById('closeBtn').onclick = () => window.close();

  const showClose = new URLSearchParams(location.search).get('standalone');

  submitBtn.addEventListener('click', () => {
    const url = videoUrlInput.value.trim();
    if(!url) return;
    
    notesResult.innerHTML = "Generating notes...";
    
    console.log("Sending payload:", JSON.stringify({url: videoUrl}))

    fetch('http://127.0.0.1:5000/summarize', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({url: "https://www.youtube.com/watch?v=3olUrSOHts0"})
    })
    .then(response => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    })
    .then(data => {
      const html = markdownToHTML(data.summary);
      notesResult.innerHTML = html;
    })
    .catch(error => {
      notesResult.innerHTML = error.message;
      console.error('FETCH ERROR:', error);
      // Add specific error messages
      if (error.message.includes('Failed to fetch')) {
        console.error('Network failure - check server connection');
      } else if (error.message.includes('certificate')) {
        console.error('Certificate issue - accept the risk in Firefox');
      }
    });
  });
});

function markdownToHTML(markdown) {

  let html = markdown.replace(/</g, '&lt;').replace(/>/g, '&gt;');

  html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

  html = html.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
  
  const lines = html.split('\n');
  let inList = false;
  let listHtml = '';

  const parsedLines = lines.map(line => {
    const trimmed = line.trim();

    if (trimmed.startsWith('*')) {
      if (!inList) {
        inList = true;
        listHtml = '<ul>';
      }

      const content = trimmed.replace(/^\*+/, '').trim();
      listHtml += `<li>${content}</li>`;
      return null;
    } else {
      if (inList) {
        inList = false;
        const finishedList = listHtml + '</ul>';
        listHtml = '';
        return finishedList + `<p>${trimmed}</p>`;
      }
      return trimmed ? `<p>${trimmed}</p>` : '';
    }
  });

  if (inList) {
    parsedLines.push(listHtml + '</ul>');
  }

  return parsedLines.filter(Boolean).join('\n');
}
