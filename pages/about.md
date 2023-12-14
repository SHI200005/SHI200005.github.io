---
layout: page
title: About
description: 不会编程
keywords: L Shi
comments: true
menu: About
permalink: /About/
---

## 关于此网站 About This Website

> Good artists copy; great artists steal. --Picasso

不是每一个进行学术写作的人都是巨佬。作者的本质是**学渣**，学不会物理，专业膜大佬。这个网站**大约**（“大约”是物理学家喜爱的词语）是 0% 的原创度，全靠拜读大佬杰作并**降维**为学渣的理解。此网站完全属于**非盈利**项目，尽管作者努力避免侵权，仍可能有做得不得当之处。如有侵权，可以联系我，我将改正。

Not everyone who writes academical articles is a nerd. The author is **unfortunately innately a dull guy** and not able to learn physics... Note that this website is approximately (a word especially liked by physicist, although I am not a physicist yet) 0% of my original material. It is built on what I've learnt from scholars and  I **reduce** it to a form I **can understand**. This website is a completely **non-profit** project, and although the author strives to avoid copyright infringement, there may still be inappropriate things. If there is any, you can contact me and I will correct it.

作者如此年轻有为(?)，以至于在还没有考虑凹人设时就建立了这个网站，那时根本没有想过用英文网站在国际舞台凹人设，所以就用中文写了好多东西。不过此网站的很多文章的特征是，把数学、物理、生物...等课程的内容联系起来，那么用一篇全中文联系一篇全英文就会有些僵硬。此外，作者还引用了很多有趣的中文网络资料，这也增加了语言转换的难度。

Note that the author started this website at such a young age that didn't consider writing in English. One of the properties of those articles is that the author has always been trying to connect the knowledge in math, physics, biology courses etc. That makes it difficult to write this blog in Chinese while the others are in English and connect them... The author also cited many interesting Chinese web sources, making the language switch more difficult...

因此，博客的默认语言是中文。双语博客的前缀是"(Zh&En)"，而英语博客的前缀是"(En)"。中文的语言风格夹带过多整活，英文收敛点er。

Therefore, the default language for the blogs is Chinese. Bilingual blogs have a "(Zh&En)" prefix, and English blogs have a "(En)" prefix. The Chinese is in a casual style but the English is more formal.

## 关于我 About Me

我是 L Shi，不务正业，无所长也不博学。与我联系：<slnsinlangmc@sina.com>

I am L Shi. I never do the things I should do. I have neither expertise in a particular thing nor a broad knowledge of everything. Contact me: <slnsinlangmc@sina.com>

L Shi 是北京人，2018-2022在南京大学完成本科学习（并作为[优秀毕业生](https://physics.nju.edu.cn/xgyd/ggtz/20220329/i220215.html)毕业（但是绩点不高）），专业为物理学（本来想拿个生物科学的辅修但是物理都学不会还敢想辅修呢？）。2022秋季起在多伦多大学攻读物理学博士学位。

L Shi came from [Beijing](https://en.wikipedia.org/wiki/Beijing) and got a bachelor's degree in science from [Nanjing University](https://en.wikipedia.org/wiki/Nanjing_University) (and graduated as an [outstanding graduate](https://physics.nju.edu.cn/xgyd/ggtz/20220329/i220215.html) (but with a *not high* GPA)), majoring in Physics (the author wanted to get a minor in Biological Sciences but **how dare** the author think about a minor when could not even learn Physics?) The author is pursuing a PhD in Physics at the University of Toronto starting Fall 2022.

这是现在我在哪：[Shi, Linan - physics.utoronto.ca](https://www.physics.utoronto.ca/members/shi-linan/)。如果需要联系我，即使是学术问题，如果和我现在在 UofT 的工作无关，也请不要用我的工作邮箱。请用我的私人邮箱。谢谢！

About my current position: [Shi, Linan - physics.utoronto.ca](https://www.physics.utoronto.ca/members/shi-linan/). Try not to contact me by my working email if it is not about UofT work, even it is something about academic. Try to contact me by my personal email. Thanks!

## 社交帐号 Social

<ul>
{% for website in site.data.social %}
<li>{{website.sitename }}：<a href="{{ website.url }}" target="_blank">@{{ website.name }}</a></li>
{% endfor %}
</ul>



## Skill Keywords

{% for skill in site.data.skills %}
### {{ skill.name }}
<div class="btn-inline">
{% for keyword in skill.keywords %}
<button class="btn btn-outline" type="button">{{ keyword }}</button>
{% endfor %}
</div>
{% endfor %}
