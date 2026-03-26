const fs = require('fs');
let content = fs.readFileSync('api.html', 'utf8');

const meApis = `
        <div class="endpoint-card">
            <div class="endpoint-header">
                <span class="method get">GET</span>
                <span class="path">/users/me</span>
                <span class="tag tag-admin">Admin</span>
                <span class="desc">내 계정 정보 조회</span>
            </div>
            <div class="endpoint-body">
                <p>현재 로그인된 사용자의 상세 정보를 조회합니다. (본인 계정 수정 시 필요한 데이터 로드용)</p>
            </div>
        </div>

        <div class="endpoint-card">
            <div class="endpoint-header">
                <span class="method put">PUT</span>
                <span class="path">/users/me</span>
                <span class="tag tag-admin">Admin</span>
                <span class="desc">내 계정 정보 수정</span>
            </div>
            <div class="endpoint-body">
                <p>현재 로그인된 사용자의 이름, 이메일 등의 기본 정보를 수정합니다.</p>
                <h4>Parameters (Body)</h4>
                <table>
                    <tr><th>Field</th><th>Type</th><th>Required</th><th>Description</th></tr>
                    <tr><td>user_name</td><td>string</td><td>Yes</td><td>변경할 유저 이름</td></tr>
                    <tr><td>email</td><td>string</td><td>Yes</td><td>변경할 연락처 이메일</td></tr>
                </table>
            </div>
        </div>

        <div class="endpoint-card">
            <div class="endpoint-header">
                <span class="method put">PUT</span>
                <span class="path">/users/me/password</span>
                <span class="tag tag-admin">Admin</span>
                <span class="desc">내 비밀번호 변경</span>
            </div>
            <div class="endpoint-body">
                <p>현재 비밀번호를 확인하고 새로운 비밀번호로 변경합니다.</p>
                <h4>Parameters (Body)</h4>
                <table>
                    <tr><th>Field</th><th>Type</th><th>Required</th><th>Description</th></tr>
                    <tr><td>currentPassword</td><td>string</td><td>Yes</td><td>현재 비밀번호</td></tr>
                    <tr><td>newPassword</td><td>string</td><td>Yes</td><td>새 비밀번호</td></tr>
                </table>
            </div>
        </div>
`;

const approvalApis = `
        <div class="endpoint-card">
            <div class="endpoint-header">
                <span class="method post">POST</span>
                <span class="path">/users/signup</span>
                <span class="tag tag-admin">Admin</span>
                <span class="desc">운영자 계정 가입 요청</span>
            </div>
            <div class="endpoint-body">
                <p>새로운 관리자/운영자 계정 가입을 요청합니다. 기본적으로 <code>PENDING</code>(대기) 상태로 생성됩니다.</p>
            </div>
        </div>

        <div class="endpoint-card">
            <div class="endpoint-header">
                <span class="method get">GET</span>
                <span class="path">/users/pending</span>
                <span class="tag tag-admin">Admin</span>
                <span class="desc">승인 대기 계정 목록 조회</span>
            </div>
            <div class="endpoint-body">
                <p>가입 후 아직 관리자 승인을 받지 못한 PENDING 상태의 사용자 목록을 조회합니다. (Account Approvals 화면용)</p>
                <p><strong>필요 권한:</strong> <code>super_admin</code></p>
            </div>
        </div>

        <div class="endpoint-card">
            <div class="endpoint-header">
                <span class="method post">POST</span>
                <span class="path">/users/{userId}/approve</span>
                <span class="tag tag-admin">Admin</span>
                <span class="desc">계정 가입 승인</span>
            </div>
            <div class="endpoint-body">
                <p>대기 중인 사용자의 가입을 승인하여 ACTIVE 상태로 변경하고 Role을 부여합니다.</p>
            </div>
        </div>

        <div class="endpoint-card">
            <div class="endpoint-header">
                <span class="method post">POST</span>
                <span class="path">/users/{userId}/reject</span>
                <span class="tag tag-admin">Admin</span>
                <span class="desc">계정 가입 거절</span>
            </div>
            <div class="endpoint-body">
                <p>대기 중인 사용자의 가입 요청을 거절합니다. (해당 정보 삭제 또는 REJECTED 상태 처리)</p>
            </div>
        </div>
`;

const usersHeader = '<h3>사용자 및 권한 관리 (Users & Permissions)</h3>';
if (!content.includes('/users/me')) {
    content = content.replace(usersHeader, usersHeader + '\n' + meApis + '\n' + approvalApis);
}

const productSection = '<h3>제품 (Products)</h3>';
const statusApis = `
        <div class="endpoint-card">
            <div class="endpoint-header">
                <span class="method" style="background:#8b5cf6; color:white; padding: 4px 8px; border-radius: 4px; font-weight: bold; margin-right: 12px; font-size: 0.85rem;">PATCH</span>
                <span class="path">/{entity}/{id}/status</span>
                <span class="tag tag-admin">Admin</span>
                <span class="desc">공통 상태 토글 (활성/비활성)</span>
            </div>
            <div class="endpoint-body">
                <p>리스트 페이지의 Active/Inactive 버튼이나 모달 등을 통해 사용되는 가벼운 상태 변경 공통 API입니다.<br>
                <code>entity</code> 경로에는 <code>users</code>, <code>products</code>, <code>packages</code>, <code>contents</code>, <code>devices</code> 등이 공통 규격으로 들어갈 수 있습니다.</p>
                <h4>Parameters (Body)</h4>
                <table>
                    <tr><th>Field</th><th>Type</th><th>Required</th><th>Description</th></tr>
                    <tr><td>status</td><td>string</td><td>Yes</td><td><code>ACTIVE</code> 또는 <code>INACTIVE</code></td></tr>
                </table>
            </div>
        </div>
`;
if (!content.includes('/{entity}/{id}/status')) {
    content = content.replace(productSection, statusApis + '\n' + productSection);
}

fs.writeFileSync('api.html', content);
console.log('API file updated!');
