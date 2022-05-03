python run_mlm.py \
    --model_name_or_path bert-base-multilingual-cased \
    --model_type bert \
    --train_file train.txt \
    --do_train \
    --num_train_epochs=5.0 \
    --output_dir output \
    --line_by_line \
    --metric_for_best_model loss \
    --greater_is_better False \
    --save_total_limit 1 \
    --save_steps 1000 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --overwrite_output_dir \