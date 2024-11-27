function downloadImages() {
    const username = document.getElementById('username').value;
    const progressBar = document.getElementById('progressBar');
    const progress = document.getElementById('progress');
    const progressText = document.getElementById('progressText');
    const resultDiv = document.getElementById('result');
    
    if (!username) {
        resultDiv.innerHTML = '<p class="error">사용자명을 입력하세요</p>';
        return;
    }

    // 진행바 초기화 및 표시
    progressBar.style.display = 'block';
    progress.style.width = '0%';
    progressText.textContent = '다운로드 중...';
    resultDiv.innerHTML = '';
    
    const formData = new FormData();
    formData.append('username', username);
    
    fetch('/download', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            startDownload(username, data.total_posts);
        } else {
            progressBar.style.display = 'none';
            resultDiv.innerHTML = `<p class="error">${data.message}</p>`;
        }
    })
    .catch(error => {
        progressBar.style.display = 'none';
        resultDiv.innerHTML = '<p class="error">오류가 발생했습니다</p>';
        console.error('Error:', error);
    });
}

function startDownload(username, totalPosts) {
    const progress = document.getElementById('progress');
    const progressText = document.getElementById('progressText');
    const resultDiv = document.getElementById('result');
    let downloaded = 0;

    const formData = new FormData();
    formData.append('username', username);

    fetch('/start_download', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            progressText.textContent = '다운로드 완료!';
            resultDiv.innerHTML = `
                <p class="success">
                    다운로드가 완료되었습니다!<br>
                    저장 위치: ${data.path}<br>
                    다운로드된 파일 수: ${data.total}개
                </p>`;
            progress.style.width = '100%';
        } else {
            progressBar.style.display = 'none';
            resultDiv.innerHTML = `<p class="error">${data.message}</p>`;
        }
    })
    .catch(error => {
        progressBar.style.display = 'none';
        resultDiv.innerHTML = '<p class="error">다운로드 중 오류가 발생했습니다</p>';
        console.error('Error:', error);
    });
}
