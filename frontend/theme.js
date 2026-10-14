// Логика переключения светлой/тёмной темы и мобильного меню (шторки)
(function () {
  const savedTheme = localStorage.getItem('wrap_toon_theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);

  function updateThemeUI() {
    const current = document.documentElement.getAttribute('data-theme');
    const isDark = current === 'dark';

    // Кнопка в десктопной шапке
    const desktopBtn = document.getElementById('theme-toggle');
    if (desktopBtn) {
      desktopBtn.textContent = isDark ? '☀️' : '🌙';
      desktopBtn.title = isDark ? 'Включить светлую тему' : 'Включить тёмную тему';
    }

    // Кнопка в мобильной шторке
    const drawerThemeBtn = document.getElementById('drawer-theme-toggle');
    if (drawerThemeBtn) {
      const icon = drawerThemeBtn.querySelector('.drawer-theme-icon');
      const text = drawerThemeBtn.querySelector('.drawer-theme-text');
      if (icon) icon.textContent = isDark ? '☀️' : '🌙';
      if (text) text.textContent = isDark ? 'Светлая тема' : 'Тёмная тема';
    }
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('wrap_toon_theme', next);
    updateThemeUI();
  }

  document.addEventListener('DOMContentLoaded', () => {
    updateThemeUI();

    // Клики по кнопкам темы
    const desktopBtn = document.getElementById('theme-toggle');
    if (desktopBtn) desktopBtn.addEventListener('click', toggleTheme);

    const drawerThemeBtn = document.getElementById('drawer-theme-toggle');
    if (drawerThemeBtn) drawerThemeBtn.addEventListener('click', toggleTheme);

    // --- МОБИЛЬНОЕ МЕНЮ (ШТОРКА) ---
    const drawer = document.getElementById('mobile-drawer');
    const openBtn = document.getElementById('mobile-menu-btn');
    const closeBtn = document.getElementById('drawer-close-btn');
    const backdrop = document.getElementById('drawer-backdrop');

    function openDrawer() {
      if (!drawer) return;
      drawer.classList.add('is-open');
      drawer.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }

    function closeDrawer() {
      if (!drawer) return;
      drawer.classList.remove('is-open');
      drawer.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    if (openBtn) openBtn.addEventListener('click', openDrawer);
    if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
    if (backdrop) backdrop.addEventListener('click', closeDrawer);

    // Закрытие по Escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && drawer && drawer.classList.contains('is-open')) {
        closeDrawer();
      }
    });

    // Закрытие шторки при переходе по ссылке внутри неё
    if (drawer) {
      drawer.querySelectorAll('.drawer-nav-link').forEach(link => {
        link.addEventListener('click', closeDrawer);
      });
    }

    // Адаптер внутренних ссылок для локальной разработки через Live Server (порт 5500)
    if (window.location.port === '5500') {
      const isSubdir = window.location.pathname.startsWith('/frontend/');
      document.querySelectorAll('a[href]').forEach(link => {
        const href = link.getAttribute('href');
        if (href && !href.startsWith('http') && !href.startsWith('#') && !href.includes('.')) {
          if (href === '/') {
            link.setAttribute('href', isSubdir ? '/frontend/index.html' : '/index.html');
          } else {
            const clean = href.replace(/^\//, '');
            link.setAttribute('href', (isSubdir ? '/frontend/' : '/') + clean + '.html');
          }
        }
      });
    }
  });
})();
