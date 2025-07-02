<div class="flex flex-col text-left font-bold gap-y-10">
<p 
  v-click="1"
  v-motion
  :initial="{ opacity: 0 }"
  :enter="{ opacity: 1}"
  :exit="{ opacity: 0 }"
  :duration="1000"
  class="text-7xl">How <span>To</span></p>
<p 
  v-click="2"
  v-motion
  :initial="{ opacity: 0 }"
  :enter="{ opacity: 1}"
  :exit="{ opacity: 0 }"
  :duration="1000"
  class="text-7xl">Edit <span class="color-orange">Text</span> <span>Without</span></p>
<p 
  v-click="3"
  v-motion
  :initial="{ opacity: 0 }"
  :enter="{ opacity: 1}"
  :exit="{ opacity: 0 }"
  :duration="1000"
  class="text-7xl">Manually <span>Repeating</span></p>
<p 
  v-click="4"
  v-motion
  :initial="{ opacity: 0 }"
  :enter="{ opacity: 1}"
  :exit="{ opacity: 0 }"
  :duration="1000"
  class="text-7xl">Commands <span>In</span> <span class="color-orange">Vim?</span></p>
</div>
