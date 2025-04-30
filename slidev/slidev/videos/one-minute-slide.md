<div class="flex flex-col items-center justify-center h-full mb-2 gap-y-2">
<p class="text-5xl font-mono">one minute<sup>*</sup> python</p>
<p v-click="1" v-motion :initial="{ opacity: 0}" :enter="{ opacity: 1 }" :leave="{ opacity: 0 }" class="text-2xl font-mono">by saral.club</p>

</div>

<div v-click="2" class="absolute bottom-2 left-1/2 -translate-x-1/2 flex flex-col items-center justify-center w-full">
  <p class="text-sm font-mono">Sometime more than a minute</p>
</div>
