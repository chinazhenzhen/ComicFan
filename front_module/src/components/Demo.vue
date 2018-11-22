<template>
  <div class="container">
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'Demo',
  data() {
    return {
      msg: '' //在这个地方加入你要插入的json数据
    }
  },
  methods: {
    getMessage () {
      // 怎样设置为本机IP
      const path = 'http://140.143.46.111:5000/demo'
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    }
  },
  created () {
    this.getMessage()
  }
}
</script>
