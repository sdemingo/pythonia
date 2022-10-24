

(defun turtle-run()
  (interactive)
  (shell-command "python3 turtle_core.py"))



(global-set-key (kbd "<f7>") 'turtle-run)
