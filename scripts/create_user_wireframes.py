import os
import glob
import re

def create_user_files():
    base_dir = r"CMS-webpage\wireframe_site"
    list_path = os.path.join(base_dir, 'user-list.html')
    editor_path = os.path.join(base_dir, 'user-editor.html')

    # Read notice-list.html to get boilerplate sidebar/header
    with open(os.path.join(base_dir, 'notice-list.html'), 'r', encoding='utf-8') as f:
        template = f.read()

    # Create user-list.html
    user_list_main = """    <main class="main-content">
      <div class="container">
        <!-- Page Header -->
        <div class="page-header">
          <div>
            <h1 class="page-title">👥 Admin Users</h1>
            <p class="page-desc">Manage system administrators, local managers, and their permissions.</p>
          </div>
          <div class="header-actions">
            <button class="btn btn-primary" onclick="location.href='user-editor.html'">+ New User</button>
          </div>
        </div>

        <!-- Filter Panel -->
        <div class="filter-panel">
          <div class="filter-group" style="flex:2">
            <label>Search</label>
            <input class="input" placeholder="🔍 Search Users (Name, ID, Email)..." style="width:100%">
          </div>
          <div class="filter-group">
            <label>Role</label>
            <select class="input" style="width:150px">
              <option>All</option>
              <option>Super</option>
              <option>Operation</option>
              <option>Local</option>
              <option>Technician</option>
            </select>
          </div>
          <div class="filter-group">
            <label>Status</label>
            <select class="input" style="width:120px">
              <option>All</option>
              <option>Active</option>
              <option>Suspended</option>
            </select>
          </div>
          <div class="filter-group">
            <label style="opacity:0">.</label>
            <button class="btn btn-outline" style="border:1px solid #d1d5db;background:#fff;color:#374151">Reset</button>
          </div>
        </div>

        <!-- List Table -->
        <table class="data-table">
          <thead>
            <tr>
              <th style="width:40px"><input type="checkbox"></th>
              <th>Login ID</th>
              <th>Name</th>
              <th>Role</th>
              <th>Email</th>
              <th>Last Login</th>
              <th>Status</th>
              <th style="text-align:right">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><input type="checkbox"></td>
              <td><strong>admin_root</strong></td>
              <td>시스템 관리자</td>
              <td><span class="badge" style="background:#e0e7ff;color:#1e40af">Super</span></td>
              <td>admin@cellbig.com</td>
              <td>2026-03-12 10:00</td>
              <td><span class="status-indicator status-active"></span>Active</td>
              <td style="text-align:right; gap:8px;">
                 <button class="btn btn-outline" onclick="location.href='user-editor.html'">Edit</button>
              </td>
            </tr>
            <tr>
              <td><input type="checkbox"></td>
              <td><strong>op_seoul</strong></td>
              <td>서울 총괄</td>
              <td><span class="badge" style="background:#dbeafe;color:#1e3a8a">Operation</span></td>
              <td>op_seoul@cellbig.com</td>
              <td>2026-03-11 15:30</td>
              <td><span class="status-indicator status-active"></span>Active</td>
              <td style="text-align:right; gap:8px;">
                 <button class="btn btn-outline" onclick="location.href='user-editor.html'">Edit</button>
              </td>
            </tr>
            <tr>
              <td><input type="checkbox"></td>
              <td><strong>loc_busan</strong></td>
              <td>부산 담당자</td>
              <td><span class="badge" style="background:#f3f4f6;color:#374151">Local</span></td>
              <td>loc_busan@cellbig.com</td>
              <td>2026-03-01 09:12</td>
              <td><span class="status-indicator status-error"></span>Suspended</td>
              <td style="text-align:right; gap:8px;">
                 <button class="btn btn-outline" onclick="location.href='user-editor.html'">Edit</button>
              </td>
            </tr>
          </tbody>
        </table>
        
        <!-- Pagination -->
        <div class="pagination" style="margin-top:20px;display:flex;justify-content:center;gap:8px">
          <button class="btn btn-outline" disabled>&lt;</button>
          <button class="btn btn-primary">1</button>
          <button class="btn btn-outline">2</button>
          <button class="btn btn-outline">&gt;</button>
        </div>
      </div>
    </main>
  </div>
  <script src="app.js"></script>
</body>
</html>"""
    
    # Replace main block
    user_list_html = re.sub(r'<main class="main-content">.*</body>\n</html>', user_list_main, template, flags=re.DOTALL)
    user_list_html = user_list_html.replace('<title>Notice List — CellbigCMS</title>', '<title>User List — CellbigCMS</title>')
    user_list_html = user_list_html.replace('data-page="notice-list.html"', 'data-page="user-list.html"')

    # Create user-editor.html
    user_editor_main = """    <main class="main-content">
      <div class="container">
        <!-- Page Header -->
        <div class="page-header" style="border-bottom:none; margin-bottom:8px">
          <div>
            <div style="font-size:14px;color:#6b7280;margin-bottom:8px;cursor:pointer" onclick="location.href='user-list.html'">← Back to Users</div>
            <h1 class="page-title">Create / Edit User</h1>
            <p class="page-desc">Create a new admin user or update existing information.</p>
          </div>
          <div class="header-actions">
            <button class="btn btn-outline" onclick="location.href='user-list.html'">Cancel</button>
            <button class="btn btn-primary" onclick="alert('User Saved!')">Save Changes</button>
          </div>
        </div>

        <div style="display:grid;grid-template-columns:2fr 1fr;gap:24px;margin-top:20px">
          <!-- Left Column -->
          <div style="display:flex;flex-direction:column;gap:24px">
            <section class="panel">
              <h3 style="margin-top:0;margin-bottom:20px;font-size:16px;border-bottom:1px solid #e5e7eb;padding-bottom:12px">👤 Account Info</h3>
              
              <div class="form-group">
                <label class="form-label">Login ID <span style="color:red">*</span></label>
                <input type="text" class="form-input" placeholder="e.g. admin_seoul" required>
              </div>

              <div class="form-group" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
                <div>
                  <label class="form-label">User Name <span style="color:red">*</span></label>
                  <input type="text" class="form-input" placeholder="e.g. 홍길동" required>
                </div>
                <div>
                  <label class="form-label">Email <span style="color:red">*</span></label>
                  <input type="email" class="form-input" placeholder="user@cellbig.com" required>
                </div>
              </div>

              <div class="form-group" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px;">
                 <div>
                    <label class="form-label">Password <span style="color:red">*</span></label>
                    <input type="password" class="form-input" placeholder="Enter new password">
                 </div>
                 <div>
                    <label class="form-label">Confirm Password</label>
                    <input type="password" class="form-input" placeholder="Verify password">
                 </div>
              </div>

              <div class="form-group">
                <label class="form-label">Description (Optional)</label>
                <textarea class="form-input" rows="3" placeholder="Additional user account information"></textarea>
              </div>
            </section>

            <section class="panel">
              <h3 style="margin-top:0;margin-bottom:20px;font-size:16px;border-bottom:1px solid #e5e7eb;padding-bottom:12px">🔐 Permission Settings</h3>
              
              <div class="form-group">
                <label class="form-label">System Role <span style="color:red">*</span></label>
                <select class="form-input" required>
                  <option disabled selected>Select a role...</option>
                  <option value="Super">Super (Master access to everything)</option>
                  <option value="Operation">Operation (High-level manager)</option>
                  <option value="Local">Local (Regional manager)</option>
                  <option value="Technician">Technician (Maintenance access)</option>
                </select>
              </div>

              <div class="form-group" style="margin-top:16px;">
                <label class="form-label">Management Scope (scopeIds)</label>
                <p style="font-size:13px;color:#6b7280;margin-bottom:8px;">Choose regions or stores this user manages. Leave blank for all access if role is "Super".</p>
                <select class="form-input" multiple style="min-height:90px;">
                  <option value="loc_seoul">Area: Seoul</option>
                  <option value="loc_busan">Area: Busan</option>
                  <option value="store_01">Store: Main Store #1</option>
                </select>
              </div>
            </section>
          </div>

          <!-- Right Column -->
          <div>
            <section class="panel">
              <h3 style="margin-top:0;margin-bottom:20px;font-size:16px;border-bottom:1px solid #e5e7eb;padding-bottom:12px">⚙️ Account Status</h3>
              
              <div class="form-group">
                <label class="form-label">Status</label>
                <select class="form-input">
                  <option value="Active">Active</option>
                  <option value="Suspended">Suspended</option>
                </select>
              </div>
            </section>
            
            <section class="panel">
               <div style="font-size:13px; color:#6b7280; line-height:1.6;">
                  Last Login: <b>2026-03-12 10:00:23</b><br/>
                  Created At: <b>2026-03-01 09:00:00</b><br/>
                  Updated At: <b>2026-03-11 15:30:10</b>
               </div>
            </section>
          </div>
        </div>
      </div>
    </main>
  </div>
  <script src="app.js"></script>
</body>
</html>"""
    
    user_editor_html = re.sub(r'<main class="main-content">.*</body>\n</html>', user_editor_main, template, flags=re.DOTALL)
    user_editor_html = user_editor_html.replace('<title>Notice List — CellbigCMS</title>', '<title>User Editor — CellbigCMS</title>')
    user_editor_html = user_editor_html.replace('data-page="notice-list.html"', 'data-page="user-editor.html"')

    with open(list_path, 'w', encoding='utf-8') as f:
        f.write(user_list_html)
    with open(editor_path, 'w', encoding='utf-8') as f:
        f.write(user_editor_html)

    print("Created user-list.html and user-editor.html")

create_user_files()

def add_user_to_sidebar():
    base_dir = r"CMS-webpage\wireframe_site"
    html_files = glob.glob(os.path.join(base_dir, '*.html'))

    for f_path in html_files:
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already added
        if 'data-page="user-list.html"' not in content:
            # We locate <div class="sidebar-item">⚙️ Settings</div> or similar and insert before it
            # The exact string might vary, let's search for "Settings</div>"
            old_str = '<div class="sidebar-category">System</div>'
            new_str = '<div class="sidebar-category">System</div>\n      <div class="sidebar-item" data-page="user-list.html">👥 Admin Users</div>'
            
            # Or insert at the top of System
            content = content.replace(old_str, new_str)
            
            with open(f_path, 'w', encoding='utf-8') as f:
                f.write(content)

    print("Added Users to sidebars of all HTML files.")

add_user_to_sidebar()
