Page({
  data: {
    search: '',
    tools: [
      { name: '口语练习', icon: 'icon-speaking', description: 'AI 陪练，强化口语表达与发音。' },
      { name: '文书评审', icon: 'icon-essay', description: '一键体检文书结构、语法与亮点。' },
      { name: '申请社区', icon: 'icon-community', description: '结识学长学姐，汲取最新申请经验。' },
      { name: '签证指南', icon: 'icon-visa', description: '快速掌握各国签证材料与流程。' },
      { name: '面试准备', icon: 'icon-interview', description: '模拟常见问答，建立自信表达。' },
      { name: '院校数据库', icon: 'icon-database', description: '精准检索全球院校与专业数据。' }
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
      : this.data.tools.filter(t => {
          const nameMatch = t.name.toLowerCase().includes(q);
          const descMatch = (t.description || '').toLowerCase().includes(q);
          return nameMatch || descMatch;
        });
    this.setData({ filteredTools: filtered });
  },
  onToolTap(e) {
    const name = e.currentTarget.dataset.name;
    wx.showToast({ title: name, icon: 'none' });
  }
});
