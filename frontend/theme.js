// Логика переключения светлой/тёмной темы с сохранением в localStorage
(function () {
  const savedTheme = localStorage.getItem('wrap_toon_theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);

  function updateThemeIcon() {
    const btn = document.getElementById('theme-toggle');
    if (!btn) return;
    const current = document.documentElement.getAttribute('data-theme');
    btn.textContent = current === 'dark' ? '☀️' : '🌙';
  }

  document.addEventListener('DOMContentLoaded', () => {
    updateThemeIcon();
    const btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('wrap_toon_theme', next);
        updateThemeIcon();
      });
    }
  });
})();
