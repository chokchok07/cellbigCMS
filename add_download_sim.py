import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Download button clicks
html = re.sub(
    r'onclick="alert\(\'다운로드 데모\'\)">⬇️ Download</button>',
    r'onclick="simulateDownload(this)">⬇️ Download</button>',
    html
)

# 2. Add JavaScript simulateDownload function and Toast HTML
toast_html = """
  <!-- Toast Notification -->
  <div id="toastContainer" style="display:none; position:fixed; bottom:20px; right:20px; background:#374151; color:#fff; padding:12px 24px; border-radius:6px; box-shadow:0 4px 6px rgba(0,0,0,0.1); z-index:9999; font-size:14px; align-items:center; gap:12px; transition:opacity 0.3s ease;">
    <div class="toast-loader" id="toastLoader" style="width:16px; height:16px; border:2px solid transparent; border-top-color:#fff; border-radius:50%; animation:toast-spin 1s linear infinite;"></div>
    <span id="toastMessage">다운로드 중입니다... (content.zip)</span>
  </div>
  
  <style>
    @keyframes toast-spin {
      to { transform: rotate(360deg); }
    }
  </style>

  <script>
    function simulateDownload(btnElement) {
      if(btnElement.disabled) return;
      
      const originalText = btnElement.innerHTML;
      btnElement.disabled = true;
      btnElement.style.opacity = '0.7';
      btnElement.innerHTML = '⏳ Loading...';
      
      // Toast 노출
      const toast = document.getElementById('toastContainer');
      const toastMsg = document.getElementById('toastMessage');
      const toastLoader = document.getElementById('toastLoader');
      
      toast.style.display = 'flex';
      toast.style.opacity = '1';
      toast.style.background = '#374151'; // 다크그레이
      toastLoader.style.display = 'block';
      toastMsg.innerText = '다운로드 중입니다... (content.zip)';
      
      // 2초 뒤 완료 처리
      setTimeout(() => {
        btnElement.innerHTML = '✅ 완료';
        btnElement.style.color = '#10b981';
        btnElement.style.borderColor = '#10b981';
        
        toastLoader.style.display = 'none';
        toast.style.background = '#10b981'; // 초록색으로 변경
        toastMsg.innerText = '다운로드가 완료되었습니다!';
        
        // 2초 뒤 토스트 닫고 버튼 복구
        setTimeout(() => {
          toast.style.opacity = '0';
          setTimeout(() => {
            toast.style.display = 'none';
            btnElement.disabled = false;
            btnElement.style.opacity = '1';
            btnElement.innerHTML = originalText;
            btnElement.style.color = '';
            btnElement.style.borderColor = '';
          }, 300);
        }, 2000);
      }, 1500);
    }
  </script>
</body>
"""

html = html.replace('</body>', toast_html)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done")