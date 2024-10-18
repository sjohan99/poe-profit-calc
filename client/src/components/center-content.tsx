export type CenterContentProps = {
  children: React.ReactNode;
  background?: string;
  className?: string;
  childrenContainerClassName?: string;
};

export function CenterContent(props: CenterContentProps) {
  const extra_styling = props.className ?? "";
  const childrenContainerClassName = props.childrenContainerClassName ?? "";
  return (
    <div className={`flex justify-center ${extra_styling}`.trim()}>
      <div className="flex-none -lg:min-w-0"></div>
      <div
        className={`max-w-screen-2xl grow rounded-sm ${props.background ?? ""}`.trim()}
      >
        <div className={`px-3 py-3 ${childrenContainerClassName}`}>
          {props.children}
        </div>
      </div>
      <div className="flex-none -lg:min-w-0"></div>
    </div>
  );
}
