"""Static assets served by the lightweight web UI server."""

INDEX_HTML = r"""<!DOCTYPE html>
<html lang=\"en\">
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>Mobipick Labs Control (Web)</title>
    <style>
      :root {
        color-scheme: dark;
        font-family: "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        background: #101014;
        color: #e9ecef;
      }
      body {
        margin: 0;
        padding: 0;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
      }
      header {
        padding: 1rem 1.5rem;
        background: #1f1f28;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        align-items: center;
        justify-content: space-between;
      }
      header h1 {
        font-size: 1.4rem;
        margin: 0;
      }
      main {
        flex: 1;
        padding: 1rem 1.5rem 2.5rem;
        display: grid;
        grid-template-columns: minmax(260px, 320px) 1fr;
        gap: 1.5rem;
      }
      @media (max-width: 1024px) {
        main {
          grid-template-columns: 1fr;
        }
      }
      .panel {
        background: #191926;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.35);
      }
      #control-panel h2,
      #layout-panel h2 {
        font-size: 1.1rem;
        margin: 0 0 0.75rem 0;
      }
      #toggle-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
        gap: 0.75rem;
      }
      .toggle-button {
        border: none;
        border-radius: 10px;
        padding: 0.8rem 0.6rem;
        font-size: 0.95rem;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.12s ease, filter 0.12s ease;
      }
      .toggle-button:disabled {
        cursor: not-allowed;
        opacity: 0.6;
      }
      .toggle-button:not(:disabled):hover {
        transform: translateY(-1px);
        filter: brightness(1.1);
      }
      .combo-group {
        margin-top: 1rem;
        display: grid;
        gap: 0.75rem;
      }
      .combo-group label {
        display: flex;
        flex-direction: column;
        gap: 0.35rem;
        font-size: 0.9rem;
      }
      .combo-group select {
        border-radius: 8px;
        padding: 0.5rem 0.6rem;
        border: 1px solid rgba(255,255,255,0.08);
        background: #1f1f2c;
        color: inherit;
      }
      #actions-row {
        margin-top: 1rem;
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
      }
      #actions-row button {
        border-radius: 8px;
        padding: 0.45rem 0.9rem;
        border: 1px solid rgba(255,255,255,0.12);
        background: transparent;
        color: inherit;
        cursor: pointer;
        transition: background 0.12s ease;
      }
      #actions-row button:hover {
        background: rgba(255,255,255,0.08);
      }
      #layout-panel {
        display: flex;
        flex-direction: column;
        gap: 1rem;
      }
      #layout-config {
        display: flex;
        flex-wrap: wrap;
        gap: 0.75rem;
        align-items: center;
      }
      #layout-config select {
        border-radius: 8px;
        padding: 0.4rem 0.7rem;
        border: 1px solid rgba(255,255,255,0.12);
        background: #1f1f2c;
        color: inherit;
      }
      #tab-selector {
        display: grid;
        gap: 0.4rem;
        grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
      }
      #tab-selector label {
        background: rgba(255,255,255,0.05);
        padding: 0.45rem 0.6rem;
        border-radius: 8px;
        display: flex;
        align-items: center;
        gap: 0.5rem;
      }
      #log-container {
        display: grid;
        gap: 1rem;
      }
      #log-container.columns-1 {
        grid-template-columns: 1fr;
      }
      #log-container.columns-2 {
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      }
      #log-container.columns-3 {
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      }
      .log-card {
        background: rgba(17, 18, 30, 0.92);
        border-radius: 12px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        border: 1px solid rgba(255,255,255,0.05);
      }
      .log-card header {
        background: rgba(255,255,255,0.05);
        padding: 0.6rem 0.85rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      .log-card header h3 {
        margin: 0;
        font-size: 1rem;
        font-weight: 600;
      }
      .log-card header button {
        border: none;
        border-radius: 6px;
        padding: 0.25rem 0.55rem;
        background: rgba(255,255,255,0.08);
        color: inherit;
        cursor: pointer;
      }
      .log-scroll {
        overflow-y: auto;
        max-height: 380px;
        padding: 0.8rem 0.85rem;
        font-family: Menlo, Consolas, "Fira Code", monospace;
        font-size: 0.85rem;
        line-height: 1.35rem;
        background: rgba(0, 0, 0, 0.35);
      }
      .log-line {
        padding-bottom: 0.2rem;
      }
      .log-line.origin-gui {
        color: #50fa7b;
      }
      .log-line.origin-container {
        color: #f8f9fa;
      }
      .status-pill {
        background: rgba(80, 250, 123, 0.15);
        border-radius: 999px;
        padding: 0.15rem 0.6rem;
        font-size: 0.8rem;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Mobipick Labs Control (Web)</h1>
      <div id=\"status-line\" class=\"status-pill\">Connecting...</div>
    </header>
    <main>
      <section id=\"control-panel\" class=\"panel\">
        <h2>Primary Controls</h2>
        <div id=\"toggle-grid\"></div>
        <div class=\"combo-group\" id=\"combo-group\"></div>
        <div id=\"actions-row\">
          <button data-action=\"refresh_status\">Refresh Status</button>
          <button data-action=\"refresh_images\">Refresh Images</button>
          <button data-action=\"refresh_scripts\">Refresh Scripts</button>
        </div>
      </section>
      <section id=\"layout-panel\" class=\"panel\">
        <div>
          <h2>Embedded Process Layout</h2>
          <div id=\"layout-config\">
            <label>
              View Mode:
              <select id=\"layout-select\">
                <option value=\"1\">Single Column</option>
                <option value=\"2\" selected>Two Columns</option>
                <option value=\"3\">Three Columns</option>
              </select>
            </label>
          </div>
        </div>
        <div>
          <h2>Visible Tabs</h2>
          <div id=\"tab-selector\"></div>
        </div>
      </section>
      <section id=\"log-panel\" class=\"panel\" style=\"grid-column: 1 / -1;\">
        <h2>Processes &amp; Logs</h2>
        <div id=\"log-container\" class=\"columns-2\"></div>
      </section>
    </main>
    <script>
      (function () {
        'use strict';

        if (typeof window.Promise !== 'function') {
          function SimplePromise(executor) {
            if (!(this instanceof SimplePromise)) {
              throw new TypeError('Promise must be called with new');
            }
            if (typeof executor !== 'function') {
              throw new TypeError('Promise executor must be a function');
            }

            var self = this;
            self._state = 'pending';
            self._value = undefined;
            self._handlers = [];

            function schedule(fn) {
              window.setTimeout(fn, 0);
            }

            function handle(handler) {
              var cb = self._state === 'fulfilled' ? handler.onFulfilled : handler.onRejected;
              if (typeof cb !== 'function') {
                if (self._state === 'fulfilled') {
                  handler.resolve(self._value);
                } else {
                  handler.reject(self._value);
                }
                return;
              }
              try {
                var result = cb(self._value);
                handler.resolve(result);
              } catch (err) {
                handler.reject(err);
              }
            }

            function runHandlers() {
              if (self._handlers.length === 0) {
                return;
              }
              var handlers = self._handlers.slice(0);
              self._handlers.length = 0;
              for (var i = 0; i < handlers.length; i += 1) {
                handle(handlers[i]);
              }
            }

            function addHandler(handler) {
              if (self._state === 'pending') {
                self._handlers.push(handler);
              } else {
                schedule(function () {
                  handle(handler);
                });
              }
            }

            function settle(state, value) {
              if (self._state !== 'pending') {
                return;
              }
              self._state = state;
              self._value = value;
              schedule(runHandlers);
            }

            function fulfill(value) {
              settle('fulfilled', value);
            }

            function reject(reason) {
              settle('rejected', reason);
            }

            function resolve(value) {
              if (value === self) {
                reject(new TypeError('Cannot resolve promise with itself'));
                return;
              }
              if (value && (typeof value === 'object' || typeof value === 'function')) {
                var then;
                try {
                  then = value.then;
                } catch (err) {
                  reject(err);
                  return;
                }
                if (typeof then === 'function') {
                  var called = false;
                  try {
                    then.call(
                      value,
                      function (val) {
                        if (called) {
                          return;
                        }
                        called = true;
                        resolve(val);
                      },
                      function (err) {
                        if (called) {
                          return;
                        }
                        called = true;
                        reject(err);
                      }
                    );
                    return;
                  } catch (err2) {
                    if (!called) {
                      reject(err2);
                    }
                    return;
                  }
                }
              }
              fulfill(value);
            }

            this._addHandler = addHandler;

            try {
              executor(resolve, reject);
            } catch (err3) {
              reject(err3);
            }
          }

          SimplePromise.prototype.then = function (onFulfilled, onRejected) {
            var self = this;
            return new SimplePromise(function (resolve, reject) {
              self._addHandler({
                onFulfilled: onFulfilled,
                onRejected: onRejected,
                resolve: resolve,
                reject: reject
              });
            });
          };

          SimplePromise.prototype.catch = function (onRejected) {
            return this.then(undefined, onRejected);
          };

          SimplePromise.resolve = function (value) {
            return new SimplePromise(function (resolve) {
              resolve(value);
            });
          };

          SimplePromise.reject = function (reason) {
            return new SimplePromise(function (_resolve, reject) {
              reject(reason);
            });
          };

          window.Promise = SimplePromise;
        }

        var state = {
          toggles: {},
          tabs: {},
          combobox: {},
          status: {},
          selectedTabs: [],
          layoutColumns: 2,
          lastEvent: 0
        };

        function hasOwn(obj, key) {
          return Object.prototype.hasOwnProperty.call(obj, key);
        }

        function isArray(value) {
          return Object.prototype.toString.call(value) === '[object Array]';
        }

        function escapeHtml(text) {
          if (text === undefined || text === null) {
            return '';
          }
          return String(text)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
        }

        function safeOriginClass(origin) {
          var value = origin || 'container';
          return value.replace(/[^a-zA-Z0-9_-]/g, '');
        }

        function hasSelectedTab(key) {
          return state.selectedTabs.indexOf(key) !== -1;
        }

        function addSelectedTab(key) {
          if (!hasSelectedTab(key)) {
            state.selectedTabs.push(key);
          }
        }

        function removeSelectedTab(key) {
          var idx = state.selectedTabs.indexOf(key);
          if (idx !== -1) {
            state.selectedTabs.splice(idx, 1);
          }
        }

        function filterSelectedTabs() {
          for (var i = state.selectedTabs.length - 1; i >= 0; i -= 1) {
            var key = state.selectedTabs[i];
            if (!hasOwn(state.tabs, key)) {
              state.selectedTabs.splice(i, 1);
            }
          }
        }

        function setStatus(text) {
          var element = document.getElementById('status-line');
          if (element) {
            element.textContent = text;
          }
        }

        function getJSON(url) {
          if (typeof window.fetch === 'function') {
            return fetch(url, { cache: 'no-store' }).then(function (res) {
              if (!res.ok) {
                throw new Error('Request failed: ' + res.status);
              }
              return res.json();
            });
          }
          return new Promise(function (resolve, reject) {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', url, true);
            xhr.setRequestHeader('Cache-Control', 'no-store');
            xhr.onreadystatechange = function () {
              if (xhr.readyState === 4) {
                if (xhr.status >= 200 && xhr.status < 300) {
                  try {
                    resolve(JSON.parse(xhr.responseText || 'null'));
                  } catch (err) {
                    reject(err);
                  }
                } else {
                  reject(new Error('Request failed: ' + xhr.status));
                }
              }
            };
            xhr.onerror = function () {
              reject(new Error('Network error'));
            };
            xhr.send(null);
          });
        }

        function postJSON(url, body) {
          if (typeof window.fetch === 'function') {
            return fetch(url, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(body)
            }).then(function (res) {
              if (!res.ok) {
                return res.text().then(function (text) {
                  throw new Error('Request failed: ' + res.status + ' ' + text);
                });
              }
              return res.json();
            });
          }
          return new Promise(function (resolve, reject) {
            var xhr = new XMLHttpRequest();
            xhr.open('POST', url, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onreadystatechange = function () {
              if (xhr.readyState === 4) {
                if (xhr.status >= 200 && xhr.status < 300) {
                  try {
                    resolve(JSON.parse(xhr.responseText || 'null'));
                  } catch (err) {
                    reject(err);
                  }
                } else {
                  reject(new Error('Request failed: ' + xhr.status + ' ' + (xhr.responseText || '')));
                }
              }
            };
            xhr.onerror = function () {
              reject(new Error('Network error'));
            };
            xhr.send(JSON.stringify(body || {}));
          });
        }

        function applySnapshot(snapshot) {
          state.toggles = snapshot && snapshot.toggles ? snapshot.toggles : {};
          state.combobox = snapshot && snapshot.combobox ? snapshot.combobox : {};
          state.status = snapshot && snapshot.status ? snapshot.status : {};
          state.tabs = {};

          var tabs = snapshot && snapshot.tabs ? snapshot.tabs : {};
          for (var key in tabs) {
            if (hasOwn(tabs, key)) {
              var tab = tabs[key] || {};
              state.tabs[key] = {
                key: key,
                label: tab.label || key,
                closable: !!tab.closable,
                logs: isArray(tab.logs) ? tab.logs.slice(0) : []
              };
            }
          }

          var events = snapshot && snapshot.events ? snapshot.events : [];
          for (var i = 0; i < events.length; i += 1) {
            var evt = events[i];
            if (evt && evt.id && evt.id > state.lastEvent) {
              state.lastEvent = evt.id;
            }
            applyEvent(evt);
          }

          if (!state.selectedTabs.length) {
            var count = 0;
            for (var tabKey in state.tabs) {
              if (hasOwn(state.tabs, tabKey)) {
                addSelectedTab(tabKey);
                count += 1;
                if (count >= 3) {
                  break;
                }
              }
            }
          }

          renderAll();
        }

        function applyEvent(evt) {
          if (!evt || !evt.type) {
            return;
          }
          var payload = evt.payload || {};
          switch (evt.type) {
            case 'toggle':
              if (payload.key) {
                state.toggles[payload.key] = payload;
              }
              break;
            case 'tab':
              if (!payload.key) {
                break;
              }
              if (hasOwn(state.tabs, payload.key)) {
                var existing = state.tabs[payload.key];
                existing.label = payload.label || existing.label;
                existing.closable = !!payload.closable;
              } else {
                state.tabs[payload.key] = {
                  key: payload.key,
                  label: payload.label || payload.key,
                  closable: !!payload.closable,
                  logs: []
                };
              }
              break;
            case 'tab_removed':
              if (payload.key && hasOwn(state.tabs, payload.key)) {
                delete state.tabs[payload.key];
                removeSelectedTab(payload.key);
              }
              break;
            case 'log':
              if (!payload.key) {
                break;
              }
              if (!hasOwn(state.tabs, payload.key)) {
                state.tabs[payload.key] = {
                  key: payload.key,
                  label: payload.key,
                  closable: true,
                  logs: []
                };
              }
              var tab = state.tabs[payload.key];
              tab.logs.push({
                html: payload.html || '',
                origin: payload.origin || 'container'
              });
              if (tab.logs.length > 400) {
                tab.logs.splice(0, tab.logs.length - 400);
              }
              break;
            case 'combobox':
              if (payload.name) {
                state.combobox[payload.name] = {
                  options: payload.options || [],
                  current: payload.current || null
                };
              }
              break;
            case 'status':
              if (payload.key) {
                state.status[payload.key] = payload.value;
              }
              break;
            case 'shutdown':
              setStatus('Application shutting down');
              break;
            default:
              break;
          }
        }

        function renderAll() {
          renderToggles();
          renderCombos();
          renderTabSelector();
          renderLogs();
          updateStatusLine();
        }

        function renderToggles() {
          var grid = document.getElementById('toggle-grid');
          if (!grid) {
            return;
          }
          grid.innerHTML = '';
          for (var key in state.toggles) {
            if (!hasOwn(state.toggles, key)) {
              continue;
            }
            var data = state.toggles[key] || {};
            var btn = document.createElement('button');
            btn.className = 'toggle-button';
            btn.setAttribute('data-toggle', key);
            btn.textContent = data.text || key;
            btn.disabled = !data.enabled;
            var colors = data.colors || {};
            var padding = colors.padding !== undefined && colors.padding !== null ? colors.padding : 6;
            btn.style.backgroundColor = colors.bg || '#343a40';
            btn.style.color = colors.fg || '#fff';
            btn.style.padding = String(padding) + 'px';
            btn.onclick = (function (toggleKey) {
              return function () {
                handleAction('toggle_' + toggleKey);
              };
            })(key);
            grid.appendChild(btn);
          }
        }

        function renderCombos() {
          var wrapper = document.getElementById('combo-group');
          if (!wrapper) {
            return;
          }
          wrapper.innerHTML = '';
          for (var name in state.combobox) {
            if (!hasOwn(state.combobox, name)) {
              continue;
            }
            var data = state.combobox[name] || {};
            var label = document.createElement('label');
            label.textContent = name + ' configuration';
            var select = document.createElement('select');
            var options = data.options || [];
            for (var i = 0; i < options.length; i += 1) {
              var opt = document.createElement('option');
              opt.value = options[i];
              opt.textContent = options[i];
              if (options[i] === data.current) {
                opt.selected = true;
              }
              select.appendChild(opt);
            }
            select.onchange = (function (comboName, element) {
              return function () {
                handleAction('set_combo', { name: comboName, value: element.value });
              };
            })(name, select);
            label.appendChild(select);
            wrapper.appendChild(label);
          }
        }

        function renderTabSelector() {
          var container = document.getElementById('tab-selector');
          if (!container) {
            return;
          }
          container.innerHTML = '';
          var tabsArray = [];
          for (var key in state.tabs) {
            if (hasOwn(state.tabs, key)) {
              tabsArray.push(state.tabs[key]);
            }
          }
          tabsArray.sort(function (a, b) {
            var aLabel = a.label || '';
            var bLabel = b.label || '';
            if (aLabel < bLabel) return -1;
            if (aLabel > bLabel) return 1;
            return 0;
          });
          for (var i = 0; i < tabsArray.length; i += 1) {
            var tab = tabsArray[i];
            var label = document.createElement('label');
            var cb = document.createElement('input');
            cb.type = 'checkbox';
            cb.checked = hasSelectedTab(tab.key);
            cb.onchange = (function (tabKey, checkbox) {
              return function () {
                if (checkbox.checked) {
                  addSelectedTab(tabKey);
                } else {
                  removeSelectedTab(tabKey);
                }
                renderLogs();
              };
            })(tab.key, cb);
            var span = document.createElement('span');
            span.textContent = tab.label;
            label.appendChild(cb);
            label.appendChild(span);
            container.appendChild(label);
          }
        }

        function renderLogs() {
          var container = document.getElementById('log-container');
          if (!container) {
            return;
          }
          filterSelectedTabs();
          container.className = 'columns-' + state.layoutColumns;
          container.innerHTML = '';
          for (var i = 0; i < state.selectedTabs.length; i += 1) {
            var key = state.selectedTabs[i];
            if (!hasOwn(state.tabs, key)) {
              continue;
            }
            var tab = state.tabs[key];
            var card = document.createElement('div');
            card.className = 'log-card';
            var header = document.createElement('header');
            var title = document.createElement('h3');
            title.textContent = tab.label;
            header.appendChild(title);
            var pop = document.createElement('button');
            pop.textContent = 'Pop-out';
            pop.onclick = (function (tabData) {
              return function () {
                openTabWindow(tabData);
              };
            })(tab);
            header.appendChild(pop);
            card.appendChild(header);
            var scroller = document.createElement('div');
            scroller.className = 'log-scroll';
            var html = '';
            for (var j = 0; j < tab.logs.length; j += 1) {
              var line = tab.logs[j] || {};
              html += '<div class="log-line origin-' + safeOriginClass(line.origin) + '">' + (line.html || '') + '</div>';
            }
            scroller.innerHTML = html;
            scroller.scrollTop = scroller.scrollHeight;
            card.appendChild(scroller);
            container.appendChild(card);
          }
        }

        function openTabWindow(tab) {
          var popup = window.open('', '_tab_' + tab.key, 'width=720,height=560');
          if (!popup) {
            return;
          }
          var label = escapeHtml(tab.label || tab.key);
          var doc = popup.document;
          doc.open();
          doc.write('<!DOCTYPE html><html><head><meta charset="utf-8" />' +
            '<title>' + label + '</title>' +
            '<style>body{background:#0b0b10;color:#f8f9fa;font-family:Menlo,monospace;padding:1rem;}' +
            'h1{font-size:1.2rem;margin-bottom:0.75rem;}div{line-height:1.35rem;font-size:0.9rem;}' +
            '.log-line{margin-bottom:0.25rem;}.origin-gui{color:#50fa7b;}</style></head><body>' +
            '<h1>' + label + '</h1><div id="log-view"></div></body></html>');
          doc.close();
          var target = doc.getElementById('log-view');
          if (target) {
            var html = '';
            for (var i = 0; i < tab.logs.length; i += 1) {
              var line = tab.logs[i] || {};
              html += '<div class="log-line ' + safeOriginClass(line.origin) + '">' + (line.html || '') + '</div>';
            }
            target.innerHTML = html;
          }
        }

        function updateStatusLine() {
          var pieces = [];
          if (hasOwn(state.toggles, 'sim')) {
            var simState = state.toggles.sim && state.toggles.sim.state ? state.toggles.sim.state : 'unknown';
            pieces.push('Sim: ' + simState);
          }
          if (hasOwn(state.toggles, 'roscore')) {
            var roscoreState = state.toggles.roscore && state.toggles.roscore.state ? state.toggles.roscore.state : 'unknown';
            pieces.push('Roscore: ' + roscoreState);
          }
          if (pieces.length) {
            setStatus(pieces.join(' • '));
          } else {
            setStatus('Ready');
          }
        }

        function handleAction(action, payload) {
          if (payload === undefined) {
            payload = {};
          }
          postJSON('/api/action', { action: action, payload: payload }).catch(function (err) {
            if (window.console && console.error) {
              console.error(err);
            }
            window.alert(err && err.message ? err.message : 'Action failed');
          });
        }

        function pollEvents() {
          getJSON('/api/events?since=' + state.lastEvent)
            .then(function (events) {
              if (!isArray(events)) {
                return;
              }
              for (var i = 0; i < events.length; i += 1) {
                var evt = events[i];
                if (evt && evt.id && evt.id > state.lastEvent) {
                  state.lastEvent = evt.id;
                }
                applyEvent(evt);
              }
              renderLogs();
              renderToggles();
              updateStatusLine();
            })
            .catch(function (err) {
              if (window.console && console.warn) {
                console.warn('Polling failed', err);
              }
              setStatus('Connection lost – retrying…');
            });
        }

        function initLayoutControls() {
          var layoutSelect = document.getElementById('layout-select');
          if (layoutSelect) {
            layoutSelect.value = String(state.layoutColumns);
            layoutSelect.onchange = function () {
              var value = parseInt(layoutSelect.value, 10);
              state.layoutColumns = isNaN(value) ? 1 : value;
              renderLogs();
            };
          }
          var actionsRow = document.getElementById('actions-row');
          if (actionsRow) {
            var buttons = actionsRow.getElementsByTagName('button');
            for (var i = 0; i < buttons.length; i += 1) {
              var btn = buttons[i];
              btn.onclick = (function (actionName) {
                return function () {
                  handleAction(actionName);
                };
              })(btn.getAttribute('data-action'));
            }
          }
        }

        function bootstrap() {
          setStatus('Connecting...');
          getJSON('/api/snapshot')
            .then(function (snapshot) {
              applySnapshot(snapshot || {});
              initLayoutControls();
              setStatus('Connected');
              pollEvents();
              setInterval(pollEvents, 1200);
            })
            .catch(function (err) {
              if (window.console && console.error) {
                console.error(err);
              }
              setStatus('Failed to connect');
            });
        }

        if (document.readyState === 'complete' || document.readyState === 'interactive') {
          setTimeout(bootstrap, 0);
        } else {
          window.addEventListener('DOMContentLoaded', bootstrap);
        }
      })();
    </script>
  </body>
</html>
"""

__all__ = ["INDEX_HTML"]

