Page({
  data: {
    isReady: true,
    isLoading: true,
    stickySearch: false,
    gridReady: false,
    search: '',
    tools: [
      { name: '口语练习', icon: 'icon-speaking', description: 'AI 陪练，强化口语表达与发音。' },
      { name: '文书评审', icon: 'icon-essay', description: '一键体检文书结构、语法与亮点。' },
      { name: '申请社区', icon: 'icon-community', description: '结识学长学姐，汲取最新申请经验。' },
      { name: '签证指南', icon: 'icon-visa', description: '快速掌握各国签证材料与流程。' },
      { name: '面试准备', icon: 'icon-interview', description: '模拟常见问答，建立自信表达。' },
      { name: '院校数据库', icon: 'icon-database', description: '精准检索全球院校与专业数据。' }
    ],
    filteredTools: [],
    skeletonSlots: [0, 1, 2, 3, 4, 5],
    emptySuggestions: ['面试准备', '口语练习', '签证指南']
  },
  onLoad() {
    this.setData({ filteredTools: this.data.tools });
    this.startSkeleton();
  },
  onReady() {
    if (!this.data.isLoading) {
      this.scheduleGridReveal();
    }
  },
  onUnload() {
    this.teardown();
  },
  onPageScroll(e) {
    const shouldStick = e.scrollTop > 12;
    if (shouldStick !== this.data.stickySearch) {
      this.setData({ stickySearch: shouldStick });
    }
  },
  onSearchInput(e) {
    const search = e.detail.value || '';
    this.setData({ search });
    this.filterTools();
  },
  onSearch() {
    this.filterTools();
  },
  filterTools() {
    const q = (this.data.search || '').trim().toLowerCase();
    const filtered = !q
      ? this.data.tools
      : this.data.tools.filter(t => {
          const nameMatch = t.name.toLowerCase().includes(q);
          const descMatch = (t.description || '').toLowerCase().includes(q);
          return nameMatch || descMatch;
        });
    const hasResults = filtered.length > 0;

    this.clearGridRevealTimer();

    this.setData({ filteredTools: filtered, gridReady: false }, () => {
      if (hasResults) {
        this.scheduleGridReveal(60);
      }
    });
  },
  onToolTap(e) {
    const detail = e.detail || {};
    const currentTarget = e.currentTarget || {};
    const name = detail.name || (currentTarget.dataset && currentTarget.dataset.name) || '';
    if (!name) return;
    wx.showToast({ title: name, icon: 'none' });
  },
  resetSearch() {
    this.clearGridRevealTimer();
    this.setData({ search: '', gridReady: false }, () => {
      this.filterTools();
    });
  },
  onEmptySuggestionTap(e) {
    const dataset = (e && e.currentTarget && e.currentTarget.dataset) || {};
    const keyword = dataset.keyword || dataset.value || '';
    if (!keyword) return;
    this.clearGridRevealTimer();
    this.setData({ search: keyword, gridReady: false }, () => {
      this.filterTools();
    });
  },
  startSkeleton() {
    this.clearLoadingTimer();
    this.setData({ isLoading: true, gridReady: false });
    this.loadingTimer = setTimeout(() => {
      this.setData({ isLoading: false }, () => {
        if (this.data.isReady) {
          this.scheduleGridReveal(80);
        }
      });
      this.loadingTimer = null;
    }, 420);
  },
  scheduleGridReveal(delay = 40) {
    if (this.data.gridReady) {
      // reset to allow re-animation when explicitly requested
      this.setData({ gridReady: false }, () => {
        this.clearGridRevealTimer();
        this.gridRevealTimer = setTimeout(() => {
          this.setData({ gridReady: true });
          this.gridRevealTimer = null;
        }, delay);
      });
      return;
    }

    this.clearGridRevealTimer();
    this.gridRevealTimer = setTimeout(() => {
      this.setData({ gridReady: true });
      this.gridRevealTimer = null;
    }, delay);
  },
  clearGridRevealTimer() {
    if (this.gridRevealTimer) {
      clearTimeout(this.gridRevealTimer);
      this.gridRevealTimer = null;
    }
  },
  clearLoadingTimer() {
    if (this.loadingTimer) {
      clearTimeout(this.loadingTimer);
      this.loadingTimer = null;
    }
  },
  teardown() {
    this.clearLoadingTimer();
    this.clearGridRevealTimer();
  }
});
