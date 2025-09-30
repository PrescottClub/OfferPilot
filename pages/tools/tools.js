Page({
  data: {
    search: '',
    tools: [
      { name: '口语练习', icon: 'icon-speaking' },
      { name: '文书评审', icon: 'icon-essay' },
      { name: '申请社区', icon: 'icon-community' },
      { name: '签证指南', icon: 'icon-visa' },
      { name: '面试准备', icon: 'icon-interview' },
      { name: '院校数据库', icon: 'icon-database' }
    ],
    filteredTools: []
  },
  onLoad() {
    this.setData({ filteredTools: this.data.tools });
  },
  onSearchInput(e) {
    this.setData({ search: e.detail.value });
    this.filterTools();
  },
  onSearch() {
    this.filterTools();
  },
  filterTools() {
    const q = (this.data.search || '').trim().toLowerCase();
    const filtered = !q
      ? this.data.tools
      : this.data.tools.filter(t => t.name.toLowerCase().includes(q));
    this.setData({ filteredTools: filtered });
  },
  onToolTap(e) {
    const name = e.currentTarget.dataset.name;
    wx.showToast({ title: name, icon: 'none' });
  }
});

