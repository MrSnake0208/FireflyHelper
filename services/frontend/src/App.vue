<template>
  <div style="background-color: rgb(0, 0, 0);">
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane v-for="tab in tabs" :key="tab.name" class="panel" :name="tab.name">
                <template #label>
                    <img :src="tab.icon" class="icon" />
                </template>
                <div class="card-container">
                  <!-- Display Element Cards based on received data -->
                  <el-card v-for="relicContent in filteredRelicContents" :key="relicContent.setName" class="apple-card">
                    <div class="card-header">
                      <div class="header-left">
                        <p>{{ relicContent.setName }}</p>
                      </div>
                      <div class="header-right">
                        <el-button type="text">删除</el-button>
                      </div>
                    </div>
                    <div slot="header" class="clearfix">
                    </div>
                    <div class="text item" v-for="tag in [relicContent.mainTag, ...relicContent.normalTags]" :key="tag.name">
                      {{ tag.name }}: {{ tag.value }}
                    </div>
                    <a class="text item">Omit: {{ relicContent.omit }}</a>
                    <h3 class="text item">Level: {{ relicContent.level }}</h3>
                    <div class="text item">Star: {{ relicContent.star }}</div>
                    <div class="text item">Equip: {{ relicContent.equip }}</div>
                  </el-card>
                </div>
      </el-tab-pane>
    </el-tabs>
  </div>
  <div>
    <el-upload
      action=""
      :on-change="updateReason"
      :auto-upload="false"
      :show-file-list="false"
      accept=".json"
      list-type="multipart/form-data"
      
    >
      <el-button size="small" type="primary">阶段原因上传</el-button>
      <div class="el-upload__tip">只能上传JSON文件</div>
    </el-upload>
  </div>
</template>

<script setup lang="ts">


import axios from 'axios';
import { ref, defineProps, onMounted, Ref,computed  } from 'vue';



import {type RelicPosition, RelicSetName, RelicStatName, RelicNormalStatName } from "@type/relic"


import headIcon from '@image/misc/HEAD.png'
import handIcon from '@image/misc/HAND.png'
import bodyIcon from '@image/misc/BODY.png'
import footIcon from '@image/misc/FOOT.png'
import objectIcon from '@image/misc/OBJECT.png'
import neckIcon from '@image/misc/NECK.png'

const tabs = [
  { name: 'head', icon: headIcon },
  { name: 'hands', icon: handIcon },
  { name: 'body', icon: bodyIcon },
  { name: 'feet', icon: footIcon },
  { name: 'planarSphere', icon: objectIcon },
  { name: 'linkRope', icon: neckIcon },
];
Object.freeze(tabs);
const activeName = ref("head" as RelicPosition)


///////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////

// 写一个上传json文件的代码

const fileList = ref([]);
const relicContents = ref([]);

const updateReason = (file, fileList) => {
  fileTransmit(file, fileList);
};

const fileTransmit = async (file, fileList, isShow) => {
  const reader = new FileReader();
  reader.readAsText(file.raw, 'UTF-8');

  reader.onload = async (evt) => {
    if (evt.target) {
      const dataJson = JSON.parse(evt.target.result);
      const apiUrl = 'http://127.0.0.1:8000/processrelicdata';

      try {
        const response = await axios.post(apiUrl, dataJson);
        console.log(response.data);

        // Update relicContents ref with the transformed relic data
        relicContents.value = response.data.map((relicData) => transformRelicData(relicData));
      } catch (error) {
        console.error('上传失败:', error);
      }
    }
  };
};


const transformRelicData = (relicData) => {
  // Your transformation logic based on IRelicContentOnly interface
  return {
    setName: relicData.set_name,
    position: relicData.position,
    star: relicData.star,
    mainTag: relicData.main_tag,
    normalTags: relicData.normal_tags,
    level: relicData.level,
    omit: relicData.omit,
    equip: relicData.equip,
  };
};

const handleClick = (tab, event) => {
  console.log(tab.props.name, event);
};

const filteredRelicContents = computed(() => {
  return relicContents.value.filter(relicContent => relicContent.position === activeName.value);
});
</script>

<style scoped>
.card-container {
  border: 1px dashed;
  display: grid;
  grid-gap: 20px;
  grid-template-columns: repeat(auto-fill, 300px);
  justify-content: center;

}

.apple-card {
  position: relative;
  margin: 10px;
  /* 设置阴影 */
  box-shadow: 20px 20px 50px rgba(0, 0, 0, 0.5);
  border-radius: 15px;
  /* 设置card的背景色 */
  background: rgba(255, 255, 255, 0.1);
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  border-top: 1px solid rgba(255, 255, 255, 0.5);
  border-left: 1px solid rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(5px);
}
.apple-card.content{
  padding: 20px;
     text-align: center;
}
.apple-card.content h2{
  position: absolute;
  top: -60px;
  right: 1px;
  font-size: 10em;
  color: rgba(255, 255, 255, 0.05);
  pointer-events: none;

}

.apple-card.content h3{
  font-size: 1.8em;
  color: #fff;
  z-index: 1;
}


.apple-card.content p{
  font-size: 1em;
     color: #fff;
     font-weight: 300;
}

.apple-card.content a{
  position: relative;
  display: inline-block;
  padding: 8px 20px;
  margin-top: 15px;
  background: #fff;
  color: #000;
  border-radius: 20px;
  text-decoration: none;
  font-weight: 500;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}
/* Media queries can be added for further customization if needed */
</style>