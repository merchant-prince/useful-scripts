#! /usr/bin/env zsh

main() {
  local script_dir="${0:a:h}"

  # shellcheck disable=SC1090
  source "${script_dir}/.env/bin/activate"

  if pip list --outdated --format=freeze |
    grep -v '^\-e' |
    cut -d '=' -f 1 |
    xargs -n1 pip install -U; then
    pip freeze >"${script_dir}/requirements.txt"
  fi
}

main
