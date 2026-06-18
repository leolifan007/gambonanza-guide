/* Gambonanza Guide — Redesign JS */
(function() {
  'use strict';

  /* ─── Mobile Nav Toggle ─── */
  const toggle = document.getElementById('nav-toggle');
  const nav = document.getElementById('main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function() {
      nav.classList.toggle('open');
    });
    /* Close nav when clicking a link */
    nav.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        nav.classList.remove('open');
      });
    });
  }

  /* ─── Sidebar Article Navigation (Ajax load) ─── */
  const sidebar = document.getElementById('category-sidebar');
  const contentArea = document.getElementById('main-content');
  if (sidebar && contentArea) {
    sidebar.addEventListener('click', function(e) {
      const link = e.target.closest('.sidebar-article-link');
      if (!link) return;
      /* If it's the current page, just do normal navigation */
      if (link.classList.contains('active')) return;

      e.preventDefault();
      const url = link.getAttribute('data-url') || link.getAttribute('href');
      if (!url) return;

      /* Update active state */
      sidebar.querySelectorAll('.sidebar-article-link.active').forEach(function(el) {
        el.classList.remove('active');
      });
      link.classList.add('active');

      /* Show loading state */
      contentArea.style.opacity = '0.5';

      fetch(url)
        .then(function(resp) { return resp.text(); })
        .then(function(html) {
          /* Extract the article body + page header from response */
          var parser = new DOMParser();
          var doc = parser.parseFromString(html, 'text/html');

          /* Update page title */
          var newTitle = doc.querySelector('title');
          if (newTitle) document.title = newTitle.textContent;

          /* Update article content */
          var newBody = doc.getElementById('article-body');
          if (newBody) {
            document.getElementById('article-body').innerHTML = newBody.innerHTML;
          }

          /* Update page header (title, description) */
          var newPageHeader = doc.querySelector('.page-header');
          var existingPageHeader = document.querySelector('.page-header');
          if (newPageHeader && existingPageHeader) {
            existingPageHeader.innerHTML = newPageHeader.innerHTML;
          }

          /* Update URL without reload */
          window.history.pushState({ url: url }, '', url);

          contentArea.style.opacity = '1';

          /* Scroll to top of content */
          contentArea.scrollTop = 0;
          window.scrollTo({ top: document.querySelector('.section').offsetTop - 100, behavior: 'smooth' });
        })
        .catch(function() {
          /* Fallback: normal navigation */
          window.location.href = url;
        });
    });

    /* Handle browser back/forward */
    window.addEventListener('popstate', function(e) {
      if (e.state && e.state.url) {
        window.location.href = e.state.url;
      }
    });
  }

  /* ─── Section Frame Wrapper ─── */
  /* Wrap content between h2 headings in .section-frame for visual section grouping */
  (function() {
    var article = document.querySelector('.content-body.article-body');
    if (!article || window.location.pathname === '/') return;
    var nodes = Array.from(article.childNodes);
    var sections = [];
    var current = null;
    nodes.forEach(function(node) {
      if (node.nodeType === 1 && node.tagName === 'H2') {
        current = { heading: node, children: [] };
        sections.push(current);
      } else if (current) {
        current.children.push(node);
      }
    });
    sections.forEach(function(s) {
      if (s.children.length === 0) return;
      var wrapper = document.createElement('div');
      wrapper.className = 'section-frame';
      s.children.forEach(function(child) {
        wrapper.appendChild(child);
      });
      s.heading.parentNode.insertBefore(wrapper, s.heading.nextSibling);
    });
  })();

})();
