import { type ReactNode } from "react";

type TooltipProps = {
  children: ReactNode;
};

export default function Tooltip({ children }: TooltipProps): JSX.Element {
  return (
    <div className="has-tooltip flex items-center">
      <div className="tooltip ml-7 flex flex-row gap-2 rounded bg-accent-1 p-1 shadow-lg">
        {children}
      </div>
      <svg
        className="h-5 min-h-5 w-5 min-w-5 fill-current text-warn"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        id="tooltip-no-arrow"
      >
        <path d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 11V9h2v6H9v-4zm0-6h2v2H9V5z" />
      </svg>
    </div>
  );
}

{
  /*  */
}
