Component({
  options: {
    styleIsolation: 'apply-shared'
  },
  externalClasses: ['row-class'],
  properties: {
    icon: {
      type: String,
      value: ''
    },
    label: {
      type: String,
      value: ''
    },
    selectable: {
      type: Boolean,
      value: false
    }
  },
  methods: {
    handleTap() {
      if (!this.data.selectable) return;
      this.triggerEvent('rowtap');
    }
  }
});
