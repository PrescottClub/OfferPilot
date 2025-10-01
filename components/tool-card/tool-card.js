Component({
  options: {
    styleIsolation: 'apply-shared'
  },
  properties: {
    name: {
      type: String,
      value: ''
    },
    icon: {
      type: String,
      value: ''
    },
    description: {
      type: String,
      value: ''
    }
  },
  methods: {
    handleTap() {
      this.triggerEvent('cardtap', { name: this.data.name });
    }
  }
});
