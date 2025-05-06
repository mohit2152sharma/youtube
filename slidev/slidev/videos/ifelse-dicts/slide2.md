<div class="flex flex-col items-start justify-center h-full">
<div class="flex flex-col items-start justify-center italic text-wrap w-3/4 text-gray-400">
    <Typewriter text='"sometimes you can see a problem in a different way and rewrite it so that a special case goes away and becomes the normal case, and thats good code."' :type-delay="50" :erase-delay="100"/>
</div>

<div class="absolute bottom-50 left-150" v-click="1" 
v-motion
:initial="{ opacity: 0 }"
:enter="{ opacity: 1}"
:duration="1000"
>
<p>- Linus Torvalds</p>
</div>
</div>