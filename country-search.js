/**
 * Searchable Country Code Dropdown
 * Replaces all <select name="country_code"> elements with a searchable dropdown.
 */
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    injectStyles();
    document.querySelectorAll('select[name="country_code"]').forEach(initSearchableSelect);
  });

  function injectStyles() {
    if (document.getElementById('cc-search-styles')) return;
    var style = document.createElement('style');
    style.id = 'cc-search-styles';
    style.innerHTML = `
      .cc-search-wrapper { position: relative; width: 100px; flex-shrink: 0; display: flex; align-items: flex-end; }
      .cc-search-btn { width: 100%; display: flex; align-items: center; justify-content: space-between; gap: 4px; padding: 9px 0; border: 0; border-bottom: 1px solid var(--line, #dbe3ea); background: transparent; color: var(--ink, #1e293b); font-size: 14px; font-family: inherit; font-weight: normal; cursor: pointer; text-align: left; transition: border-color .2s; }
      .cc-search-btn:hover, .cc-search-wrapper-open .cc-search-btn { border-color: var(--blue, #1d5368); }
      .cc-search-arrow { font-size: 11px; color: var(--muted, #64748b); transition: transform .2s; }
      .cc-search-wrapper-open .cc-search-arrow { transform: rotate(180deg); }
      .cc-search-dropdown { display: none; position: absolute; top: calc(100% + 4px); left: 0; width: 220px; background: var(--white, #fff); border: 1px solid var(--line, #dbe3ea); border-radius: 8px; box-shadow: 0 12px 36px rgba(0,0,0,.12); z-index: 10000; overflow: hidden; }
      .cc-search-dropdown-open { display: block; }
      .cc-search-input { width: 100%; padding: 10px 12px; border: 0 !important; border-bottom: 1px solid var(--line, #dbe3ea) !important; outline: none; font-size: 13px; background: var(--grey, #f8f8f8); color: var(--ink, #1e293b); box-sizing: border-box; }
      .cc-search-input::placeholder { color: var(--muted, #64748b); }
      .cc-search-list { max-height: 220px; overflow-y: auto; background: #fff; }
      .cc-search-list::-webkit-scrollbar { width: 5px; }
      .cc-search-list::-webkit-scrollbar-track { background: transparent; }
      .cc-search-list::-webkit-scrollbar-thumb { background: var(--line, #dbe3ea); border-radius: 3px; }
      .cc-search-item { padding: 8px 12px; font-size: 13px; cursor: pointer; transition: background .15s; color: #1e293b; }
      .cc-search-item:hover { background: var(--grey, #f1f5f9); }
      .cc-search-item-active { background: var(--yellow-soft, #fff8d8); font-weight: 600; }
      .cc-search-empty { padding: 16px 12px; font-size: 13px; color: var(--muted, #64748b); text-align: center; }
    `;
    document.head.appendChild(style);
  }

  function initSearchableSelect(originalSelect) {
    // Gather options
    var options = [];
    var selectedValue = '';
    var selectedLabel = '';
    for (var i = 0; i < originalSelect.options.length; i++) {
      var opt = originalSelect.options[i];
      options.push({ value: opt.value, label: opt.textContent });
      if (opt.selected) {
        selectedValue = opt.value;
        selectedLabel = opt.textContent;
      }
    }
    if (!selectedLabel && options.length) {
      selectedValue = options[0].value;
      selectedLabel = options[0].label;
    }

    // Hide original select
    originalSelect.style.display = 'none';
    originalSelect.removeAttribute('required');

    // Create wrapper
    var wrapper = document.createElement('div');
    wrapper.className = 'cc-search-wrapper';

    // Create hidden input to hold value for form submission
    var hiddenInput = document.createElement('input');
    hiddenInput.type = 'hidden';
    hiddenInput.name = 'country_code';
    hiddenInput.value = selectedValue;
    originalSelect.name = '_country_code_original';

    // Create display button
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'cc-search-btn';
    btn.innerHTML = '<span class="cc-search-btn-text">' + selectedLabel + '</span><span class="cc-search-arrow">▾</span>';

    // Create dropdown panel
    var dropdown = document.createElement('div');
    dropdown.className = 'cc-search-dropdown';

    // Search input
    var searchInput = document.createElement('input');
    searchInput.type = 'text';
    searchInput.className = 'cc-search-input';
    searchInput.placeholder = 'Search country code...';
    searchInput.autocomplete = 'off';

    // List container
    var listContainer = document.createElement('div');
    listContainer.className = 'cc-search-list';

    function renderOptions(filter) {
      listContainer.innerHTML = '';
      var filterLower = (filter || '').toLowerCase();
      var count = 0;
      options.forEach(function (opt) {
        if (filterLower && opt.label.toLowerCase().indexOf(filterLower) === -1 && opt.value.indexOf(filterLower) === -1) {
          return;
        }
        count++;
        var item = document.createElement('div');
        item.className = 'cc-search-item' + (opt.value === hiddenInput.value ? ' cc-search-item-active' : '');
        item.textContent = opt.label;
        item.setAttribute('data-value', opt.value);
        item.addEventListener('click', function () {
          selectOption(opt);
        });
        listContainer.appendChild(item);
      });
      if (count === 0) {
        var empty = document.createElement('div');
        empty.className = 'cc-search-empty';
        empty.textContent = 'No results found';
        listContainer.appendChild(empty);
      }
    }

    function selectOption(opt) {
      hiddenInput.value = opt.value;
      originalSelect.value = opt.value;
      btn.querySelector('.cc-search-btn-text').textContent = opt.label;
      closeDropdown();
    }

    function openDropdown() {
      dropdown.classList.add('cc-search-dropdown-open');
      wrapper.classList.add('cc-search-wrapper-open');
      searchInput.value = '';
      renderOptions('');
      setTimeout(function () { searchInput.focus(); }, 30);
    }

    function closeDropdown() {
      dropdown.classList.remove('cc-search-dropdown-open');
      wrapper.classList.remove('cc-search-wrapper-open');
    }

    function toggleDropdown() {
      if (dropdown.classList.contains('cc-search-dropdown-open')) {
        closeDropdown();
      } else {
        openDropdown();
      }
    }

    // Events
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      toggleDropdown();
    });

    searchInput.addEventListener('input', function () {
      renderOptions(this.value);
    });

    searchInput.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeDropdown();
      if (e.key === 'Enter') {
        e.preventDefault();
        var first = listContainer.querySelector('.cc-search-item');
        if (first) first.click();
      }
    });

    // Close on outside click
    document.addEventListener('click', function (e) {
      if (!wrapper.contains(e.target)) {
        closeDropdown();
      }
    });

    // Assemble
    dropdown.appendChild(searchInput);
    dropdown.appendChild(listContainer);
    wrapper.appendChild(hiddenInput);
    wrapper.appendChild(btn);
    wrapper.appendChild(dropdown);

    // Insert after original select
    originalSelect.parentNode.insertBefore(wrapper, originalSelect.nextSibling);

    // Initial render
    renderOptions('');
  }
})();
