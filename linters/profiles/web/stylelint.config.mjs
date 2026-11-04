export default {
  extends: ["stylelint-config-standard"],
  defaultSeverity: "error",
  reportDescriptionlessDisables: true,
  reportInvalidScopeDisables: true,
  reportNeedlessDisables: true,
  reportUnscopedDisables: true,
  rules: {
    "declaration-no-important": true,
    "selector-max-id": 0,
  },
};
