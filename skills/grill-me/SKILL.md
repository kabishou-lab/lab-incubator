---
name: grill-me
description: Relentless design-tree interview. Use when planning, choosing architecture, splitting tasks, or scope is unclear. Also when the user says grill / grill-me. Do not write a solution first.
---

# grill-me

规划、选架构、拆任务、范围不清时强制使用。按 `NOW.md` 写代码、修 bug、提交推送时不要用。

未达用户确认的共识前：不写方案、不拆实现任务当交付、不改业务代码。

事实（仓库、文档、运行现状）自己查，不要拿能查到的问题去问用户。

## 树与轮次

把问题建成**设计树**：每个决策下面挂依赖它的决策。

按**轮**推进。**frontier** = 前提已定、现在就能问、不必猜未答之题的全部决策。一轮问完整条 frontier：每题编号，并给出推荐答案。等用户回答后再开下一轮。

本轮仍未决的题，不能作为本轮另一题的前提——那种题放到下一轮。

格式：

```
❓ **Q1** - **<标题>**: <题干，可含选项>

➡️ <推荐答案>

---

❓ **Q2** - **<标题>**: <题干>

➡️ <推荐答案>
```

用户作答后重算 frontier。决策归用户；查找归你。

frontier 为空：每条分支都走过，没有默许假设。复述共识，**等用户确认后再动手**。

## 共识落点（本实验室）

- 覆盖写入仓库根的 `NOW.md`（当前 / 下一步）
- 仅不可逆决策才追加 `decisions/ADR-*.md`
- `journal/YYYY-MM.md` 只记一两行：grill 了什么、结论是什么
- 不建 `grilling/` 目录，不把问答全文另存一份
