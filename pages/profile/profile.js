const PROFILE_STORAGE_KEY = 'offerPilot.profile.v1';
const PROFILE_FIELDS = ['nickname', 'name', 'regions', 'score', 'schools', 'majors'];

function extractProfileFields(source) {
  const target = {};
  PROFILE_FIELDS.forEach(key => {
    if (Object.prototype.hasOwnProperty.call(source, key)) {
      target[key] = source[key];
    }
  });
  return target;
}

function loadProfileFromStorage() {
  try {
    const stored = wx.getStorageSync(PROFILE_STORAGE_KEY);
    if (!stored || typeof stored !== 'object') {
      return null;
    }
    return extractProfileFields(stored);
  } catch (err) {
    console.warn('Failed to load profile from storage', err);
    return null;
  }
}

function persistProfileSnapshot(data) {
  const payload = extractProfileFields(data);
  try {
    wx.setStorageSync(PROFILE_STORAGE_KEY, payload);
    return true;
  } catch (err) {
    console.warn('Failed to save profile to storage', err);
    return false;
  }
}

Page({
  data: {
    nickname: '',
    name: '',
    regions: [],
    regionsExpanded: false,
    allRegions: ['美国', '加拿大', '英国', '法国', '德国', '澳大利亚', '新西兰'],
    regionFlags: {
      '美国': 'flag-us',
      '加拿大': 'flag-ca',
      '英国': 'flag-uk',
      '法国': 'flag-fr',
      '德国': 'flag-de',
      '澳大利亚': 'flag-au',
      '新西兰': 'flag-nz'
    },
    score: '',
    schools: '',
    majors: ''
  },
  onLoad() {
    const stored = loadProfileFromStorage();
    if (stored) {
      this.setData(stored);
    }
  },
  onName(e) {
    const value = e.detail.value;
    this.setData({ name: value }, () => {
      this.persistProfile();
    });
  },
  onRegions(e) {
    const value = e.detail.value;
    this.setData({ regions: value }, () => {
      this.persistProfile();
    });
  },
  onScore(e) {
    const value = e.detail.value;
    this.setData({ score: value }, () => {
      this.persistProfile();
    });
  },
  onSchools(e) {
    const value = e.detail.value;
    this.setData({ schools: value }, () => {
      this.persistProfile();
    });
  },
  onMajors(e) {
    const value = e.detail.value;
    this.setData({ majors: value }, () => {
      this.persistProfile();
    });
  },
  toggleRegions() {
    this.setData({ regionsExpanded: !this.data.regionsExpanded });
  },
  onSave() {
    const ok = this.persistProfile();
    wx.showToast({ title: ok ? '已保存' : '保存失败', icon: ok ? 'success' : 'none' });
  },
  persistProfile() {
    return persistProfileSnapshot(this.data);
  }
});
