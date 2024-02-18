<template>
  <div style="background-color: black;">
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane v-for="tab in tabs" :key="tab.name" :label="tab.name" :icon="tab.icon">
        <template #label>
                    <img :src="tab.icon" class="icon" style="color: blue;" />
                </template>
        <div>{{ tab.name }} content</div>
      </el-tab-pane>
    </el-tabs>
  </div>
  <div>
    <el-upload
      action
      :on-change="updateReason"
      :auto-upload="false"
      accept=".json"
      list-type="multipart/form-data"
    >
      <el-button size="small" type="primary">阶段原因上传</el-button>
      <div slot="tip" class="el-upload__tip">只能上传JSON文件</div>
    </el-upload>
  </div>
</template>

<script setup lang="ts">




import headIcon from '@image/misc/HEAD.png'
import handIcon from '@image/misc/HAND.png'
import bodyIcon from '@image/misc/BODY.png'
import footIcon from '@image/misc/FOOT.png'
import objectIcon from '@image/misc/OBJECT.png'
import neckIcon from '@image/misc/NECK.png'


const tabs = [
  { name: 'Head', icon: headIcon },
  { name: 'Hand', icon: handIcon },
  { name: 'Body', icon: bodyIcon },
  { name: 'Foot', icon: footIcon },
  { name: 'Object', icon: objectIcon },
  { name: 'Neck', icon: neckIcon },
];
Object.freeze(tabs);
let activeName = 'Head';



import axios from 'axios';
import { ref, defineProps, onMounted } from 'vue';

const props = defineProps(/* your props here */);
const fileList = ref([]);

const updateReason = (file: any, fileList: any) => {
  fileTransmit(file, fileList);
};

const fileTransmit = async (file: any, fileList: any, isShow?: boolean) => {
  fileList = fileList;
  const reader = new FileReader();
  reader.readAsText(file.raw, 'UTF-8');

  reader.onload = async (evt) => {
    if (evt.target) {
      const dataJson = JSON.parse(evt.target.result as string);
      const apiUrl = 'http://127.0.0.1:8000/processrelicdata';

      try {
        const response = await axios.post(apiUrl, dataJson);
        console.log(response.data);
      } catch (error) {
        console.error('上传失败:', error);
      }
    }
  };
};



const handleClick = (tab, event) => {
  console.log(tab.name, event);
};


</script>
